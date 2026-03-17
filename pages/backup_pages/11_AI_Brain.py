
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.ai_master_brain_v2 import run_ai_master_brain
    
    
    st.set_page_config(page_title="AI Hotel Brain", layout="wide")
    
    st.title("🧠 AI Hotel Brain")
    
    st.subheader("Global AI Revenue Intelligence")
    
    
    data = run_ai_master_brain()
    
    
    # =============================
    # CORE METRICS
    # =============================
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Demand Index", data["demand_index"])
    col2.metric("Recommended Price €", data["recommended_price"])
    col3.metric("Market Position", data["market_position"])
    
    
    st.divider()
    
    
    # =============================
    # STRATEGY
    # =============================
    
    st.subheader("Revenue Strategy")
    
    st.write(data["strategy"])
    st.write(data["recommendation"])
    
    
    st.divider()
    
    
    # =============================
    # RISK
    # =============================
    
    st.subheader("Revenue Risk")
    
    st.write("Risk Level:", data["risk_level"])
    st.write("Reason:", data["risk_reason"])
    
    
    st.divider()
    
    
    # =============================
    # TOTAL REVENUE
    # =============================
    
    st.subheader("Total Revenue")
    
    st.metric("Total Revenue €", int(data["total_revenue"]))
    
    
    # =============================
    # AI ALERTS
    # =============================
    
    st.subheader("AI Alerts")
    
    alerts = []
    
    if data["demand_index"] > 0.8:
        alerts.append("🔥 High demand detected")
    
    if data["market_position"] == "Below market":
        alerts.append("📉 Price below market")
    
    if data["risk_level"] == "High":
        alerts.append("⚠ High revenue risk")
    
    if alerts:
        for a in alerts:
            st.warning(a)
    else:
        st.success("No critical alerts")

# fallback
if __name__ == "__main__":
    render()
