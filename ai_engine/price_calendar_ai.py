import pandas as pd
from datetime import datetime, timedelta

from ai_engine.automatic_pricing_engine import automatic_price


def generate_price_calendar(days=30):

    calendar = []

    base_price = automatic_price(
        120,
        "datasets/competitor_rates.csv",
        "datasets/bookings.csv"
    )

    start_date = datetime.today()

    for i in range(days):

        date = start_date + timedelta(days=i)

        price = base_price * (1 + (i * 0.01))

        calendar.append({
            "date": date.strftime("%Y-%m-%d"),
            "recommended_price": round(price, 2)
        })

    return calendar
