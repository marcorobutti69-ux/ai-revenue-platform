import pandas as pd


def calculate_revenue_kpi():

    bookings = pd.read_csv("datasets/bookings.csv")

    available_rooms = 100

    rooms_sold_total = bookings["rooms_sold"].sum()

    days = bookings["date"].nunique()

    avg_rooms_sold_day = rooms_sold_total / days

    occupancy = avg_rooms_sold_day / available_rooms

    # prezzo medio
    if "avg_price" in bookings.columns:
        adr = bookings["avg_price"].mean()

    elif "price" in bookings.columns:
        adr = bookings["price"].mean()

    else:
        adr = 0

    revpar = adr * occupancy

    return {
        "occupancy": round(occupancy * 100, 2),
        "adr": round(adr, 2),
        "revpar": round(revpar, 2)
    }
