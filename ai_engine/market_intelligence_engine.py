import pandas as pd


def run_market_intelligence():

    report = {}

    competitors = pd.read_csv("datasets/competitor_rates.csv")

    avg_price = competitors["price"].mean()
    min_price = competitors["price"].min()
    max_price = competitors["price"].max()

    market_range = max_price - min_price

    report["market_avg_price"] = float(round(avg_price,2))
    report["lowest_price"] = float(min_price)
    report["highest_price"] = float(max_price)
    report["market_range"] = float(market_range)

    return report
