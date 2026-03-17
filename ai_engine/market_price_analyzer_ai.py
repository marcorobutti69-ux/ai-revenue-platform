import pandas as pd

def analyze_market_prices():

    df = pd.read_csv("datasets/competitor_rates.csv")

    avg_price = df["price"].mean()
    min_price = df["price"].min()
    max_price = df["price"].max()

    return {
        "market_average": round(avg_price,2),
        "lowest_price": min_price,
        "highest_price": max_price
    }
