import pandas as pd


def demand_forecast(bookings_file):

    bookings = pd.read_csv(bookings_file)

    # Total bookings
    rooms_sold = bookings["rooms_sold"].sum()

    # Simple demand forecast logic
    available_rooms = 100

    occupancy_rate = rooms_sold / available_rooms

    demand_index = min(occupancy_rate, 1)

    forecast = {}

    forecast["rooms_sold_total"] = int(rooms_sold)
    forecast["future_demand_index"] = float(round(demand_index,2))

    if demand_index > 0.8:
        forecast["demand_level"] = "High demand expected"

    elif demand_index > 0.5:
        forecast["demand_level"] = "Moderate demand expected"

    else:
        forecast["demand_level"] = "Low demand expected"

    return forecast
