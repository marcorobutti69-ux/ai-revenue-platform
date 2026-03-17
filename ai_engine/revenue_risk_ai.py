import pandas as pd


def detect_revenue_risk():

    bookings = pd.read_csv("datasets/bookings.csv")
    competitors = pd.read_csv("datasets/competitor_rates.csv")

    rooms_sold = bookings["rooms_sold"].sum()

    avg_market_price = competitors["price"].mean()

    available_rooms = 100
    occupancy_rate = rooms_sold / available_rooms

    demand_index = min(occupancy_rate, 1)

    recommended_price = avg_market_price * (1 + demand_index * 0.1)

    if demand_index < 0.3:
        risk_level = "High"
        reason = "Low demand detected"
        suggested_action = "Launch promotions or reduce price"

    elif recommended_price > avg_market_price * 1.3:
        risk_level = "Medium"
        reason = "Price significantly above market"
        suggested_action = "Monitor competitor reaction"

    else:
        risk_level = "Low"
        reason = "Price aligned with market and demand"
        suggested_action = "Maintain current pricing"

    return {
        "risk_level": risk_level,
        "reason": reason,
        "suggested_action": suggested_action
    }
