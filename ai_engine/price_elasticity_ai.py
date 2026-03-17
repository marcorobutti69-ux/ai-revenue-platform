import pandas as pd

def calculate_price_elasticity(df):

    df = df.sort_values("price")

    price_change = df["price"].pct_change()
    demand_change = df["rooms_sold"].pct_change()

    elasticity = (demand_change / price_change).mean()

    return elasticity


def elasticity_interpretation(elasticity):

    if elasticity < -1:
        return "High price sensitivity"

    elif -1 <= elasticity < 0:
        return "Moderate price sensitivity"

    else:
        return "Low price sensitivity"


def run_price_elasticity():

    df = pd.read_csv("datasets/price_history.csv")

    elasticity = calculate_price_elasticity(df)

    interpretation = elasticity_interpretation(elasticity)

    return {
        "elasticity": round(elasticity,2),
        "interpretation": interpretation
    }
