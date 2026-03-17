def calculate_price_from_forecast(forecast_rooms, total_rooms=100, base_price=100):
    occupancy = forecast_rooms / total_rooms

    if occupancy > 0.85:
        multiplier = 1.3
    elif occupancy > 0.7:
        multiplier = 1.2
    elif occupancy > 0.5:
        multiplier = 1.1
    elif occupancy > 0.3:
        multiplier = 0.95
    else:
        multiplier = 0.8

    price = base_price * multiplier

    return round(price, 2), occupancy
