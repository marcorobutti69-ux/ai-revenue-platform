import pandas as pd


def detect_price_opportunity(hotel_price):

    competitors = pd.read_csv("datasets/competitor_rates.csv")

    avg_price = competitors["price"].mean()
    min_price = competitors["price"].min()
    max_price = competitors["price"].max()

    opportunity = {}

    opportunity["hotel_price"] = float(hotel_price)
    opportunity["market_average"] = float(round(avg_price,2))

    if hotel_price < min_price:
        opportunity["position"] = "Below all competitors"
        opportunity["suggestion"] = "Price extremely low – increase price"

    elif hotel_price < avg_price:
        opportunity["position"] = "Below market average"
        opportunity["suggestion"] = "Opportunity to increase price"

    elif hotel_price > max_price:
        opportunity["position"] = "Above all competitors"
        opportunity["suggestion"] = "Price very high – check demand"

    else:
        opportunity["position"] = "Inside market range"
        opportunity["suggestion"] = "Competitive price"

    return opportunity
