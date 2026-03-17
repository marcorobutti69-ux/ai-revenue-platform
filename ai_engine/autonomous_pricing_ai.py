import pandas as pd
from ai_engine.price_elasticity_ai import run_price_elasticity
from ai_engine.market_price_analyzer_ai import analyze_market_prices


def calculate_smart_price(base_price, demand_index, market_avg, min_price, max_price, elasticity):

    price = base_price

    # DEMAND LOGIC
    if demand_index > 1:
        price *= 1.10
    elif demand_index < 1:
        price *= 0.90

    # MARKET POSITION LOGIC
    if price < market_avg:
        price *= 1.05
    elif price > market_avg:
        price *= 0.95

    # COMPETITOR RANGE CONTROL
    if price < min_price:
        price = min_price + 2
    if price > max_price:
        price = max_price - 2

    # ELASTICITY LOGIC
    if elasticity < -1:
        price *= 0.95

    return round(price,2)


def run_autonomous_pricing():

    # base price
    base_price = 150

    # demand (simulato per ora)
    demand_index = 1.2

    # MARKET DATA
    market = analyze_market_prices()

    market_avg = market["market_average"]
    min_price = market["lowest_price"]
    max_price = market["highest_price"]

    # ELASTICITY
    elasticity_result = run_price_elasticity()
    elasticity = elasticity_result["elasticity"]

    recommended_price = calculate_smart_price(
        base_price,
        demand_index,
        market_avg,
        min_price,
        max_price,
        elasticity
    )

    return {
        "base_price": base_price,
        "market_avg": market_avg,
        "min_price": min_price,
        "max_price": max_price,
        "demand_index": demand_index,
        "elasticity": elasticity,
        "recommended_price": recommended_price
    }
