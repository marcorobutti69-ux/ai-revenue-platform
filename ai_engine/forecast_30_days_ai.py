import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_30_day_forecast():

    bookings = pd.read_csv("datasets/bookings.csv")
    competitors = pd.read_csv("datasets/competitor_rates.csv")

    avg_market_price = competitors["price"].mean()

    avg_rooms = bookings["rooms_sold"].mean()

    forecast = []

    today = datetime.today()

    for i in range(30):

        date = today + timedelta(days=i)

        demand = max(0, avg_rooms + np.random.randint(-10, 10))

        available_rooms = 100
        demand_index = min(demand / available_rooms, 1)

        recommended_price = avg_market_price * (1 + demand_index * 0.1)

        revenue = demand * recommended_price

        forecast.append({
            "date": date.strftime("%Y-%m-%d"),
            "forecast_demand": int(demand),
            "recommended_price": round(recommended_price, 2),
            "forecast_revenue": round(revenue, 2)
        })

    return forecast
