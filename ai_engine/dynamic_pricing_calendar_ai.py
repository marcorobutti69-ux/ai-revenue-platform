import pandas as pd


def generate_pricing_calendar():

    bookings = pd.read_csv("datasets/bookings.csv")
    competitors = pd.read_csv("datasets/competitor_rates.csv")

    avg_market_price = competitors["price"].mean()

    calendar = []

    grouped = bookings.groupby("date")["rooms_sold"].sum().reset_index()

    for _, row in grouped.iterrows():

        date = row["date"]
        rooms = row["rooms_sold"]

        available_rooms = 100
        demand_index = min(rooms / available_rooms, 1)

        recommended_price = avg_market_price * (1 + demand_index * 0.1)

        if demand_index > 0.8:
            demand_level = "High"
        elif demand_index < 0.3:
            demand_level = "Low"
        else:
            demand_level = "Medium"

        calendar.append({
            "date": date,
            "demand": demand_level,
            "recommended_price": round(recommended_price, 2)
        })

    return calendar
