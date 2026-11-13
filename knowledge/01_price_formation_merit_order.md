# Price formation and the merit order

## The day-ahead auction
The German-Luxembourg bidding zone (DE-LU) trades day-ahead electricity in the pan-European Single Day-Ahead Coupling (SDAC). The auction closes at 12:00 CET on the day before delivery and the results are published around 12:45-13:00. Since 1 October 2025 the day-ahead market clears in 15-minute periods (Market Time Unit, MTU); before that, prices were hourly. The harmonised SDAC price limits are -500 EUR/MWh (floor) and a ceiling of several thousand EUR/MWh. The ceiling is raised automatically after scarcity events, so check the current value with the exchange.

## The merit order
Generators bid roughly at their short-run marginal cost. Sorting bids from cheapest to most expensive gives the supply curve, called the merit order. Approximate ordering in Germany: wind and solar (near-zero marginal cost) -> nuclear (phased out in April 2023) -> lignite -> hard coal -> combined-cycle gas -> open-cycle gas turbines and oil. The price in each period is set by the most expensive unit needed to meet demand (the marginal unit), adjusted for imports and exports through market coupling.

## Residual load: the single most useful driver
Residual load = demand minus wind and solar generation. It is the part of demand that dispatchable plants (coal, gas, biomass, hydro, storage) and imports must cover. High residual load pushes the clearing price up the merit order toward gas plants; low or negative residual load pushes it toward zero or below. In Germany, day-ahead prices typically show a strong positive correlation with forecast residual load.

## Forecasts versus actuals
The day-ahead price is formed on the day before delivery, using forecasts of load, wind and solar. When explaining a day-ahead price, compare it with the day-ahead forecast residual load, not the realised one. Differences between forecast and actual values show up in the intraday and balancing markets, not in the day-ahead price.

## Fuel and carbon prices
Gas (TTF hub) and carbon (EU ETS allowance, EUA) prices set the cost of the marginal thermal plants and therefore the general price level. These prices are not in the ENTSO-E Transparency Platform. If the price level of a day is unusual and the residual load does not explain it, fuel or carbon prices are a likely reason. In that case the briefing must state that this hypothesis was not checked with data.

## Working with 15-minute prices
- A day has 96 quarter-hours (92 on the spring DST change day, 100 on the autumn one). Each price is valid for one 15-minute delivery period; a time such as 13:15 labels the start of the period.
- Quarter-hour prices are more extreme than hourly averages: short evening ramps and midday dips that used to be averaged away now show up as separate spikes or negative blocks. Comparing the maximum quarter-hour price with the maximum hourly average shows how much an hourly view would hide.
- Energy per interval is MW x 0.25 h. Four consecutive quarter-hours make one hour, so "negative for 8 quarter-hours" means two hours.
- The steep morning and evening ramps of the duck curve are often visible as large price jumps between neighbouring quarter-hours, especially at the full hour when many hourly products and unit schedules change.
