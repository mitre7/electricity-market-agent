"""Build the offline Parquet cache used as a fallback by the lecture notebook.

Usage (from the repo root):
    ENTSOE_API_KEY=... python scripts/build_cache.py 2025-01-20 2026-05-01
    python scripts/build_cache.py            # rebuilds the default lecture dates

The fetch/transform logic is intentionally identical to the notebook's
`fetch_day_live()` so cached and live data have the same shape.

Resolution: native 15-minute market time units (MTU), i.e. 96 rows per day
(92 / 100 on the DST change days). Only delivery days from 2025-10-01 onwards
(the start of 15-minute day-ahead trading) are supported. Nothing is averaged.
"""
import os
import sys
from pathlib import Path

import pandas as pd
from entsoe import EntsoePandasClient

TZ = "Europe/Berlin"
ZONE = "DE_LU"
CACHE_DIR = Path(__file__).resolve().parents[1] / "data" / "cache"

MTU_START = "2025-10-01"  # first delivery day with 15-minute day-ahead prices

DEFAULT_DATES = [
    "2025-11-25",  # winter scarcity: highest daily average of the winter, evening peak
    "2026-03-29",  # spring DST change: only 92 quarter-hours (23-hour day)
    "2026-04-05",  # Easter Sunday: negative prices for ~17 hours
    "2026-05-01",  # Labour Day holiday + solar: prices at the -500 floor
    "2026-06-24",  # summer weekday with a steep evening spike
    "2026-09-14",  # Monday with the highest peak price of the autumn
    "2026-11-04",  # recent autumn weekday with a high price level
]


def day_bounds(day):
    if pd.Timestamp(day) < pd.Timestamp(MTU_START):
        raise ValueError(f"{day}: only delivery days from {MTU_START} (15-minute MTU) are supported")
    start = pd.Timestamp(day).tz_localize(TZ)
    end = (pd.Timestamp(day) + pd.Timedelta(days=1)).tz_localize(TZ)  # DST-safe
    return start, end


def _snake(name):
    return (name.lower().replace("/", "_").replace("-", "_").replace(" ", "_")
            .replace("__", "_"))


def fetch_day_live(client, day, zone=ZONE):
    """Query ENTSO-E for one delivery day and return (15-min frame, price_history)."""
    start, end = day_bounds(day)
    clip = lambda x: x[(x.index >= start) & (x.index < end)]

    prices = clip(client.query_day_ahead_prices(zone, start=start, end=end))
    load = clip(client.query_load_and_forecast(zone, start=start, end=end))
    ws_fc = clip(client.query_wind_and_solar_forecast(zone, start=start, end=end))
    gen = clip(client.query_generation(zone, start=start, end=end))
    netpos = clip(client.query_net_position(zone, start=start, end=end, dayahead=True))

    # 30 calendar days back (720 absolute hours would add a partial day across DST), not before the 15-min era
    hist_start = max(pd.Timestamp(day) - pd.Timedelta(days=30), pd.Timestamp(MTU_START)).tz_localize(TZ)
    hist = client.query_day_ahead_prices(zone, start=hist_start, end=end)
    hist = hist[(hist.index >= hist_start) & (hist.index < end)]

    # Generation: keep "Actual Aggregated" (output), drop pumped-storage consumption.
    if isinstance(gen.columns, pd.MultiIndex):
        gen = gen.xs("Actual Aggregated", axis=1, level=1)
    gen = gen.rename(columns=lambda c: "gen_" + _snake(c))

    # Everything is natively 15-minute. This only puts all series on one regular 15-min grid
    # (forward-fill, max 3 steps) in case a series is ever published at a coarser resolution.
    h = lambda x: x.resample("15min").ffill(limit=3)
    frame = pd.DataFrame({
        "price_eur_mwh": h(prices),
        "load_actual_mw": h(load["Actual Load"]),
        "load_forecast_mw": h(load["Forecasted Load"]),
        "solar_forecast_mw": h(ws_fc.get("Solar")),
        "wind_onshore_forecast_mw": h(ws_fc.get("Wind Onshore")),
        "wind_offshore_forecast_mw": h(ws_fc.get("Wind Offshore")),
        "net_position_mw": h(netpos),  # > 0 = net export, < 0 = net import
    })
    frame = frame.join(h(gen))
    frame.index.name = "time"
    history = hist.to_frame("price_eur_mwh")
    history.index.name = "time"
    return frame, history


def main(dates):
    key = os.environ.get("ENTSOE_API_KEY")
    if not key:
        try:
            from dotenv import load_dotenv
            load_dotenv(Path(__file__).resolve().parents[1] / ".env")
            key = os.environ.get("ENTSOE_API_KEY")
        except ImportError:
            pass
    if not key:
        sys.exit("Set ENTSOE_API_KEY (env var or .env file).")
    client = EntsoePandasClient(api_key=key)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    for day in dates:
        print(f"Fetching {day} ...", flush=True)
        frame, history = fetch_day_live(client, day)
        frame.to_parquet(CACHE_DIR / f"{ZONE}_{day}.parquet")
        history.to_parquet(CACHE_DIR / f"{ZONE}_{day}_price_history.parquet")
        print(f"  {len(frame)} 15-min rows, {frame.shape[1]} columns, "
              f"avg price {frame['price_eur_mwh'].mean():.1f} EUR/MWh")


if __name__ == "__main__":
    main(sys.argv[1:] or DEFAULT_DATES)
