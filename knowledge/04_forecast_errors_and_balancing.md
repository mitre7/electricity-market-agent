# Forecast errors and balancing

## Which forecasts matter
ENTSO-E publishes the day-ahead forecasts for total load, wind onshore, wind offshore and solar for each bidding zone. TSOs and market participants use them when bidding into the day-ahead auction. Actual values are published afterwards.

## Sign convention used in this notebook
Forecast error = actual - forecast.
- Load error > 0: demand was higher than expected. This tightens the system, so intraday and imbalance prices tend to be higher.
- Wind or solar error < 0: less renewable output than forecast. This also tightens the system.
- The "residual load error" combines both: (actual load - actual RES) - (forecast load - forecast RES). A positive value means more dispatchable generation or imports were needed than planned at the day-ahead stage.

## Typical error magnitudes (Germany)
- Day-ahead solar forecast errors are largest on days with fog, snow cover or uncertain cloud cover. Errors of several GW are common in spring and summer.
- Wind forecast errors grow with wind speed uncertainty, especially when weather fronts pass. Errors of 3-8 GW in individual hours (or quarter-hours) happen several times per month.
- Load forecasts are usually accurate to within a few percent. A known problem: much rooftop PV is "behind the meter", which makes reported load sensitive to solar forecast errors.
- Note: the ENTSO-E "actual" generation for wind and solar is itself partly an estimate and can be revised.

## Why traders care
Big day-ahead forecast errors create imbalances that must be fixed in the intraday continuous market or settled at the imbalance price (reBAP in Germany). A morning briefing should flag the hours with the largest residual-load error, because those are the hours where intraday prices most likely deviated from day-ahead.
