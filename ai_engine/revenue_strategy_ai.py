import pandas as pd


def generate_revenue_strategy():

    bookings = pd.read_csv("datasets/bookings.csv")
    competitors = pd.read_csv("datasets/competitor_rates.csv")

    rooms_sold = bookings["rooms_sold"].sum()

    avg_market_price = competitors["price"].mean()

    available_rooms = 100
    occupancy_rate = rooms_sold / available_rooms

    demand_index = min(occupancy_rate, 1)

    recommended_price = avg_market_price * (1 + demand_index * 0.1)

    if demand_index > 0.7:
        action = "Maintain high price"
        recommendation = "Demand strong – keep premium positioning"

    elif demand_index < 0.3:
        action = "Reduce price / promotions"
        recommendation = "Low demand – stimulate bookings"

    else:
        action = "Maintain price"
        recommendation = "Balanced demand"

    return {
        "recommended_price": round(recommended_price, 2),
        "market_average": round(avg_market_price, 2),
        "action": action,
        "recommendation": recommendation
    }
