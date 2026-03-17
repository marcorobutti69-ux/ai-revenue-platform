import pandas as pd
from datetime import datetime, timedelta

from ai_engine.autonomous_pricing_ai import run_autonomous_pricing


def generate_price_forecast(days=30):

    forecast = []

    base_result = run_autonomous_pricing()
    base_price = base_result["recommended_price"]

    current_date = datetime.now()

    for i in range(days):

        date = current_date + timedelta(days=i)

        # simulazione variazione domanda
        demand_factor = 1 + (i * 0.01)

        forecast_price = base_price * demand_factor

        forecast.append({
            "date": date.strftime("%Y-%m-%d"),
            "forecast_price": round(forecast_price,2)
        })

    return pd.DataFrame(forecast)
