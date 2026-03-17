from main.ai_demand_forecast import AIDemandForecast

forecast_engine = AIDemandForecast("datasets/bookings.csv")

forecast_engine.train_model()

forecast = forecast_engine.forecast(30)

print(forecast[['ds','yhat']].tail())
