
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.ai_master_brain_v2 import run_ai_master_brain
    from ai_engine.revenue_risk_ai import detect_revenue_risk
    from ai_engine.opportunity_scanner_ai import scan_revenue_opportunities
    from ai_engine.total_revenue_optimizer_ai import optimize_total_revenue
    
    
    st.set_page_config(page_title="AI Revenue Command Center", layout="wide")
    
    st.title("🧠 AI Revenue Command Center")
    
    
    # ==============================
    # AI MASTER BRAIN
    # ==============================
    
    data = run_ai_master_brain()
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Demand Index", data["demand_index"])
    col2.metric("Recommended Price €", data["recommended_price"])
    col3.metric("Market Position", data["market_position"])
    
    st.write("Strategy:", data["strategy"])
    st.write("Recommendation:", data["recommendation"])
    
    st.divider()
    
    
    # ==============================
    # REVENUE RISK
    # ==============================
    
    st.subheader("⚠ Revenue Risk")
    
    risk = detect_revenue_risk()
    
    st.write("Risk Level:", risk["risk_level"])
    st.write("Reason:", risk["reason"])
    st.write("Suggested Action:", risk["suggested_action"])
    
    st.divider()
    
    
    # ==============================
    # REVENUE OPPORTUNITIES
    # ==============================
    
    st.subheader("🚀 Revenue Opportunities")
    
    opportunities = scan_revenue_opportunities()
    
    if opportunities:
        for op in opportunities[:5]:
            st.write(op["date"], "-", op["type"])
    else:
        st.write("No opportunities detected")
    
    st.divider()
    
    
    # ==============================
    # TOTAL REVENUE
    # ==============================
    
    st.subheader("💰 Total Revenue")
    
    total = optimize_total_revenue("datasets/total_revenue.csv")
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Rooms Revenue", int(total["rooms_revenue"]))
    col2.metric("F&B Revenue", int(total["fnb_revenue"]))
    col3.metric("Spa Revenue", int(total["spa_revenue"]))
    
    col4, col5, col6 = st.columns(3)
    
    col4.metric("Events Revenue", int(total["events_revenue"]))
    col5.metric("Excursions Revenue", int(total["excursions_revenue"]))
    col6.metric("Transfers Revenue", int(total["transfer_revenue"]))
    
    st.metric("Total Revenue", int(total["total_revenue"]))

# fallback
if __name__ == "__main__":
    render()
