def check_alerts(data):

    alerts = []

    if data["demand_index"] > 1.3:
        alerts.append("High demand detected")

    if data["elasticity"] < -1:
        alerts.append("High price sensitivity")

    if data["recommended_price"] < data["market_avg"]:
        alerts.append("Price below market")

    return alerts
