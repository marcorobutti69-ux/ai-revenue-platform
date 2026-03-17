import pandas as pd


def analyze_portfolio():

    portfolio = pd.read_csv("datasets/portfolio_revenue.csv")

    # calcolo revenue
    portfolio["revenue"] = portfolio["rooms_sold"] * portfolio["avg_price"]

    summary = {}

    total_revenue = portfolio["revenue"].sum()
    avg_revenue = portfolio["revenue"].mean()

    best_hotel = portfolio.loc[portfolio["revenue"].idxmax()]["hotel"]
    worst_hotel = portfolio.loc[portfolio["revenue"].idxmin()]["hotel"]

    summary["total_revenue"] = float(total_revenue)
    summary["average_revenue"] = float(avg_revenue)
    summary["best_hotel"] = best_hotel
    summary["worst_hotel"] = worst_hotel

    return summary
