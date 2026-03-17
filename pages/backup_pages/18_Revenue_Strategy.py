
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.revenue_strategy_ai import generate_revenue_strategy
    
    
    st.set_page_config(page_title="Revenue Strategy", layout="wide")
    
    st.title("📈 AI Revenue Strategy")
    
    st.subheader("AI Pricing Strategy Recommendation")
    
    
    data = generate_revenue_strategy()
    
    
    col1, col2 = st.columns(2)
    
    col1.metric("Recommended Price €", data["recommended_price"])
    col2.metric("Market Average €", data["market_average"])
    
    
    st.divider()
    
    st.subheader("Strategy Action")
    
    st.success(data["action"])
    
    
    st.subheader("Recommendation")
    
    st.write(data["recommendation"])

# fallback
if __name__ == "__main__":
    render()
