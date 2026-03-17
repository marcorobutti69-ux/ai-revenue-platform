from ai_engine.ai_autonomous_revenue_manager import run_autonomous_revenue_manager
from ai_engine.revenue_strategy_ai import generate_revenue_strategy
from ai_engine.revenue_risk_ai import detect_revenue_risk
from ai_engine.total_revenue_optimizer_ai import optimize_total_revenue


def run_ai_master_brain():

    report = {}

    # Autonomous Revenue Manager
    rm = run_autonomous_revenue_manager()

    # Revenue Strategy
    strategy = generate_revenue_strategy()

    # Revenue Risk
    risk = detect_revenue_risk()

    # Total Revenue
    total_revenue = optimize_total_revenue("datasets/total_revenue.csv")

    report["recommended_price"] = rm["recommended_price"]
    report["demand_index"] = rm["demand_index"]
    report["market_position"] = rm["market_position"]

    report["strategy"] = strategy["action"]
    report["recommendation"] = strategy["recommendation"]

    report["risk_level"] = risk["risk_level"]
    report["risk_reason"] = risk["reason"]

    report["total_revenue"] = total_revenue["total_revenue"]

    return report
