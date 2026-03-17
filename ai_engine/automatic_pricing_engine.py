import pandas as pd


def automatic_price(current_price, competitor_file, bookings_file):

    # Load datasets
    competitors = pd.read_csv(competitor_file)
    bookings = pd.read_csv(bookings_file)

    # Market analysis
    market_avg = competitors["price"].mean()
    market_min = competitors["price"].min()
    market_max = competitors["price"].max()

    # Booking demand
    rooms_sold = bookings["rooms_sold"].sum()

    # Simple demand index
    available_rooms = 100
    occupancy_rate = rooms_sold / available_rooms
    demand_index = min(occupancy_rate, 1)

    # Pricing logic
    new_price = current_price

    if demand_index > 0.8:
        new_price = market_avg * 1.10

    elif demand_index > 0.6:
        new_price = market_avg * 1.05

    elif demand_index < 0.3:
        new_price = market_avg * 0.90

    # Market boundaries
    if new_price < market_min:
        new_price = market_min

    if new_price > market_max * 1.20:
        new_price = market_max * 1.20

    return float(round(new_price, 2))
