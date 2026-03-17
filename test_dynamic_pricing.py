from ai_engine.dynamic_pricing import DynamicPricingEngine

pricing = DynamicPricingEngine(base_price=120)

price = pricing.calculate_price(
    demand_index=1.2,
    occupancy_rate=0.85,
    booking_pace=1.1
)

print("Recommended price:", price)
