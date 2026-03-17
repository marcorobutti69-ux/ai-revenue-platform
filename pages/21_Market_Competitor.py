
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.market_intelligence_engine import run_market_intelligence
    
    
    st.set_page_config(page_title="Market Competitor Intelligence", layout="wide")
    
    st.title("🌍 Market Competitor Intelligence")
    
    st.subheader("Competitor Price Analysis")
    
    
    data = run_market_intelligence()
    
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Market Average €", data["market_avg_price"])
    col2.metric("Lowest Price €", data["lowest_price"])
    col3.metric("Highest Price €", data["highest_price"])
    
    
    st.divider()
    
    st.subheader("Market Range")
    
    st.write(f"Price Range: €{data['market_range']}")

# fallback
if __name__ == "__main__":
    render()
