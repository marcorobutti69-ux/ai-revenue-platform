
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.revenue_strategy_ai import generate_revenue_strategy
    from ai_engine.revenue_risk_ai import detect_revenue_risk
    from ai_engine.ai_autonomous_revenue_manager import run_autonomous_revenue_manager
    
    
    st.set_page_config(page_title="Daily Revenue Briefing", layout="wide")
    
    st.title("📊 Daily Revenue Briefing")
    
    
    # ==============================
    # AI AUTONOMOUS REVENUE MANAGER
    # ==============================
    
    st.subheader("🤖 AI Revenue Manager Report")
    
    ai_report = run_autonomous_revenue_manager()
    
    col1, col2 = st.columns(2)
    
    col1.metric("Recommended Price €", ai_report["recommended_price"])
    col2.metric("Demand Index", ai_report["demand_index"])
    
    st.write("Market Position:", ai_report["market_position"])
    st.write("Competitor Average €:", ai_report["competitor_avg"])
    st.write("Strategy:", ai_report["strategy"])
    
    st.divider()
    
    
    # ==============================
    # REVENUE STRATEGY
    # ==============================
    
    strategy = generate_revenue_strategy()
    
    st.subheader("Revenue Strategy")
    
    col1, col2 = st.columns(2)
    
    col1.metric("Recommended Price €", strategy["recommended_price"])
    col2.metric("Market Average €", strategy["market_average"])
    
    st.write("Action:", strategy["action"])
    st.write("Recommendation:", strategy["recommendation"])
    
    st.divider()
    
    
    # ==============================
    # REVENUE RISK
    # ==============================
    
    risk = detect_revenue_risk()
    
    st.subheader("Revenue Risk")
    
    st.write("Risk Level:", risk["risk_level"])
    st.write("Reason:", risk["reason"])
    st.write("Suggested Action:", risk["suggested_action"])

# fallback
if __name__ == "__main__":
    render()
