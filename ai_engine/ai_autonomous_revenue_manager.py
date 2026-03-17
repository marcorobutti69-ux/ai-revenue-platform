import pandas as pd


def run_autonomous_revenue_manager():

    report = {}

    try:
        bookings = pd.read_csv("datasets/bookings.csv")
        competitors = pd.read_csv("datasets/competitor_rates.csv")

    except Exception as e:
        return {"error": str(e)}

    # Rooms sold
    rooms_sold = bookings["rooms_sold"].sum()

    # Competitor analysis
    avg_comp_price = competitors["price"].mean()
    min_comp_price = competitors["price"].min()
    max_comp_price = competitors["price"].max()

    # Demand index
    available_rooms = 100
    occupancy_rate = rooms_sold / available_rooms
    demand_index = min(occupancy_rate, 1)

    # Recommended price
    recommended_price = avg_comp_price * (1 + demand_index * 0.1)

    # Market position
    if recommended_price < min_comp_price:
        position = "Below market"
    elif recommended_price > max_comp_price:
        position = "Above market"
    else:
        position = "Inside market range"

    # Strategy
    if demand_index > 0.7:
        strategy = "Increase price and restrict discounts"
    elif demand_index < 0.3:
        strategy = "Launch promotions and increase visibility"
    else:
        strategy = "Maintain current pricing strategy"

    report["rooms_sold"] = int(rooms_sold)
    report["demand_index"] = float(round(demand_index, 2))
    report["recommended_price"] = float(round(recommended_price, 2))
    report["market_position"] = position
    report["competitor_avg"] = float(round(avg_comp_price, 2))
    report["strategy"] = strategy

    return report
