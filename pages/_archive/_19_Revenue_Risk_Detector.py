
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.revenue_risk_ai import detect_revenue_risk
    
    
    st.set_page_config(page_title="Revenue Risk Detector", layout="wide")
    
    st.title("⚠ AI Revenue Risk Detector")
    
    st.subheader("AI Revenue Risk Analysis")
    
    
    data = detect_revenue_risk()
    
    
    col1, col2 = st.columns(2)
    
    col1.metric("Risk Level", data["risk_level"])
    col2.write(f"Reason: {data['reason']}")
    
    
    st.divider()
    
    st.subheader("Suggested Action")
    
    st.success(data["suggested_action"])

# fallback
if __name__ == "__main__":
    render()
