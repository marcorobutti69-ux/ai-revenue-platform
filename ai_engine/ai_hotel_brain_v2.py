from ai_engine.ai_autonomous_revenue_manager import run_autonomous_revenue_manager
from ai_engine.market_intelligence_engine import run_market_intelligence
from ai_engine.price_opportunity_engine import detect_price_opportunity


def run_ai_hotel_brain():

    report = {}

    revenue = run_autonomous_revenue_manager()
    market = run_market_intelligence()

    hotel_price = revenue["recommended_price"]

    opportunity = detect_price_opportunity(hotel_price)

    report["demand_index"] = revenue["demand_index"]
    report["recommended_price"] = hotel_price
    report["market_average"] = market["market_avg_price"]
    report["price_position"] = opportunity["position"]
    report["ai_strategy"] = opportunity["suggestion"]

    return report

