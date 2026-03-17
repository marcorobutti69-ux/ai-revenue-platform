import pandas as pd

def generate_forecast(df, days=7):
    df = df.copy()

    # media mobile semplice
    df["forecast"] = df["rooms_sold"].rolling(3).mean()

    last_value = df["forecast"].iloc[-1]

    future_dates = pd.date_range(
        start=df["date"].iloc[-1],
        periods=days+1
    )[1:]

    forecast_values = [last_value for _ in range(days)]

    forecast_df = pd.DataFrame({
        "date": future_dates,
        "forecast_rooms": forecast_values
    })

    return forecast_df
