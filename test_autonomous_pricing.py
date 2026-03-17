from ai_engine.autonomous_pricing_ai import run_autonomous_pricing

result = run_autonomous_pricing()

print("Base price:", result["base_price"])
print("Market avg:", result["market_avg"])
print("Min price:", result["min_price"])
print("Max price:", result["max_price"])
print("Demand index:", result["demand_index"])
print("Elasticity:", result["elasticity"])
print("AI Recommended price:", result["recommended_price"])
