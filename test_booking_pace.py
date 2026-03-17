from main.booking_pace_forecast import BookingPaceForecast

engine = BookingPaceForecast("datasets/booking_pace.csv")

pace = engine.booking_pace()

print(pace)
