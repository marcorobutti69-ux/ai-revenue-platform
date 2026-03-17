from ai_engine.ai_revenue_engine import AIRevenueEngine

engine = AIRevenueEngine(
    bookings_dataset="datasets/bookings.csv",
    pace_dataset="datasets/booking_pace.csv"
)

result = engine.run_full_analysis()

print("Recommended price:", result["recommended_price"])
