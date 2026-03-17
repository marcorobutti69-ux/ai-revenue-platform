
import streamlit as st

def render():
    import streamlit as st
    from ai_engine.demand_radar_ai import run_demand_radar
    
    st.set_page_config(page_title="AI Demand Radar", layout="wide")
    
    st.title("📡 AI Demand Radar")
    
    st.subheader("Future Demand Signals")
    
    signals = run_demand_radar()
    
    if signals:
    
        for s in signals[:20]:
            st.write(s["date"], "—", s["type"])
    
    else:
        st.success("No demand signals detected")

# fallback
if __name__ == "__main__":
    render()
