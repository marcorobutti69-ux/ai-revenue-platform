from ai_engine.ai_master_brain_v2 import run_ai_master_brain


def generate_revenue_alerts():

    data = run_ai_master_brain()

    alerts = []

    if data["demand_index"] > 0.8:
        alerts.append("🔥 High demand spike detected")

    if data["market_position"] == "Below market":
        alerts.append("📉 Your price is below market")

    if data["risk_level"] == "High":
        alerts.append("⚠ High revenue risk")

    if data["recommended_price"] > 180:
        alerts.append("🚀 High revenue opportunity")

    return alerts
