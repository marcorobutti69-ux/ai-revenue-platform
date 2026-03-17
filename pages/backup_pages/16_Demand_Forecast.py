
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.demand_forecast_ai import demand_forecast
    
    
    st.set_page_config(page_title="Demand Forecast", layout="wide")
    
    st.title("📊 AI Demand Forecast")
    
    st.subheader("Future Demand Prediction")
    
    
    data = demand_forecast("datasets/bookings.csv")
    
    
    col1, col2 = st.columns(2)
    
    col1.metric("Rooms Sold Total", data["rooms_sold_total"])
    col2.metric("Future Demand Index", data["future_demand_index"])
    
    
    st.divider()
    
    st.subheader("Demand Level")
    
    st.success(data["demand_level"])

# fallback
if __name__ == "__main__":
    render()
