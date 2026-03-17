import pandas as pd
from datetime import datetime, timedelta

from ai_engine.autonomous_pricing_ai import run_autonomous_pricing
from ai_engine.alert_system_ai import check_alerts
from ai_engine.pms_connector import send_price_to_pms


def run_daily_pricing():

    result = run_autonomous_pricing()

    # gestione date intelligente
    try:
        df_existing = pd.read_csv("datasets/price_recommendations.csv")
        last_date = pd.to_datetime(df_existing["date"]).max()
        today = (last_date + timedelta(days=1)).strftime("%Y-%m-%d")
    except:
        today = datetime.now().strftime("%Y-%m-%d")

    data = {
        "date": today,
        "recommended_price": result["recommended_price"],
        "demand_index": result["demand_index"],
        "elasticity": result["elasticity"],
        "market_avg": result["market_avg"]
    }

    return data


def save_pricing_decision():

    file_path = "datasets/price_recommendations.csv"

    try:
        df = pd.read_csv(file_path)
    except:
        df = pd.DataFrame()

    new_data = run_daily_pricing()

    # ALERTS
    alerts = check_alerts(new_data)
    new_data["alerts"] = ", ".join(alerts)

    # PMS SIMULATION
    pms_response = send_price_to_pms(new_data["recommended_price"])
    new_data["pms_status"] = pms_response["status"]

    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    df.to_csv(file_path, index=False)

    return new_data
