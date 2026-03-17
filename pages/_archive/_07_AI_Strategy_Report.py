
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.ai_autonomous_revenue_manager import run_autonomous_revenue_manager
    
    
    st.set_page_config(page_title="AI Strategy Report", layout="wide")
    
    st.title("📈 AI Strategy Report")
    
    st.subheader("Autonomous Revenue Strategy")
    
    
    # RUN AI
    data = run_autonomous_revenue_manager()
    
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Rooms Sold", data["rooms_sold"])
    col2.metric("Demand Index", data["demand_index"])
    col3.metric("Recommended Price €", data["recommended_price"])
    
    
    st.divider()
    
    st.subheader("Market Position")
    st.write(data["market_position"])
    
    st.subheader("Strategy Recommendation")
    st.success(data["strategy"])

# fallback
if __name__ == "__main__":
    render()
