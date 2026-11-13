# Morning briefing playbook

## Purpose
A morning market briefing tells traders, analysts or operators in about two minutes what happened, why it happened, and what to watch. Every claim must be supported by data or a cited reference.

## Recommended structure
1. **Headline**: one sentence summarising the day, e.g. "Solar-driven negative prices on a holiday, followed by a steep evening ramp."
2. **Key numbers**: baseload average, peak and off-peak averages, minimum and maximum quarter-hour price with start times, the number of negative quarter-hours (and the hours they add up to), and how the day compares with the previous 30 days.
3. **Drivers**: the role of residual load, wind and solar, demand (weekday, weekend or holiday), and imports and exports. Name the times where the driver mattered most.
4. **Forecast errors**: the largest misses in load, wind and solar. Explain what they imply for intraday and imbalance prices.
5. **Context**: link to known patterns (duck curve, Dunkelflaute, holiday effect) from the knowledge base.
6. **Watch list**: two or three concrete things to monitor next.
7. **Caveats**: missing data, and drivers that could not be checked (e.g. gas and carbon prices are not in ENTSO-E data).

## Analyst heuristics
- Peak hours are 08:00-20:00 on weekdays. Base is all hours of the day (96 quarter-hours).
- Prices are per 15-minute interval. Say when an extreme lasted only a few quarter-hours, and name the interval start time.
- A correlation above 0.8 between price and forecast residual load means fundamentals explain the day well. A low correlation suggests other drivers: interconnector constraints, fuel prices, strategic bidding or outages.
- The slope of price against residual load (EUR/MWh per GW) shows how steep the merit order was that day.
- Compare the day's average price with the 30-day distribution. A z-score above 2 or below -2 is unusual.
- Never invent numbers. If a value is not in a tool result, say it is unknown.
