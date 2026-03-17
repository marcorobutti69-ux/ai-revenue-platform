import pandas as pd
from prophet import Prophet


def run_price_forecast():

    df = pd.read_csv("datasets/price_recommendations.csv")

    df = df.rename(columns={
        "date": "ds",
        "recommended_price": "y"
    })

    df["ds"] = pd.to_datetime(df["ds"])

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)

    forecast = model.predict(future)

    result = forecast[["ds", "yhat"]].tail(30)

    result = result.rename(columns={
        "ds": "date",
        "yhat": "forecast_price"
    })

    return result
