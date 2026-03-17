from ai_engine.market_price_analyzer_ai import analyze_market_prices

result = analyze_market_prices()

print("Market average:", result["market_average"])
print("Lowest competitor:", result["lowest_price"])
print("Highest competitor:", result["highest_price"])
