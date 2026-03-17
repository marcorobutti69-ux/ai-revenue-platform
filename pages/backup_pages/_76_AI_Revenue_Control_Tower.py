
import streamlit as st

def render():
    import streamlit as st
    from ai_engine.autonomous_pricing_ai import run_autonomous_pricing
    
    st.title("AI Revenue Control Tower")
    
    result = run_autonomous_pricing()
    
    st.metric("AI Recommended Price", result["recommended_price"])
    
    st.subheader("Market Overview")
    st.write("Market Average:", result["market_avg"])
    st.write("Min Price:", result["min_price"])
    st.write("Max Price:", result["max_price"])
    
    st.subheader("Demand & Elasticity")
    st.write("Demand Index:", result["demand_index"])
    st.write("Elasticity:", result["elasticity"])
    
    # STRATEGY LOGIC
    if result["elasticity"] < -1:
        st.warning("High price sensitivity → avoid aggressive pricing")
    
    if result["demand_index"] > 1:
        st.success("High demand detected")
    
    if result["recommended_price"] < result["market_avg"]:
        st.info("Competitive pricing strategy")

# fallback
if __name__ == "__main__":
    render()
