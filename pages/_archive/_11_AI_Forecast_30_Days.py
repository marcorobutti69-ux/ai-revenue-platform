
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    import altair as alt
    
    from ai_engine.forecast_30_days_ai import generate_30_day_forecast
    
    
    st.set_page_config(page_title="AI 30 Day Forecast", layout="wide")
    
    st.title("📈 AI 30-Day Revenue Forecast")
    
    forecast = generate_30_day_forecast()
    
    df = pd.DataFrame(forecast)
    
    st.dataframe(df, use_container_width=True)
    
    
    st.subheader("Demand Forecast")
    
    chart = alt.Chart(df).mark_line().encode(
        x="date:T",
        y="forecast_demand:Q",
        tooltip=["date", "forecast_demand"]
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    
    st.subheader("Revenue Forecast")
    
    chart2 = alt.Chart(df).mark_line().encode(
        x="date:T",
        y="forecast_revenue:Q",
        tooltip=["date", "forecast_revenue"]
    )
    
    st.altair_chart(chart2, use_container_width=True)

# fallback
if __name__ == "__main__":
    render()
