
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.revenue_alerts_ai import generate_revenue_alerts
    
    st.set_page_config(page_title="AI Revenue Alerts", layout="wide")
    
    st.title("🚨 AI Revenue Alerts")
    
    alerts = generate_revenue_alerts()
    
    if alerts:
    
        st.audio("assets/alert.mp3")
    
        for alert in alerts:
            st.warning(alert)
    
    else:
        st.success("No alerts detected")

# fallback
if __name__ == "__main__":
    render()
