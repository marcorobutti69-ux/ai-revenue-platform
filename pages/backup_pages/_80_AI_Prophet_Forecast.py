
import streamlit as st

def render():
    import streamlit as st
    from ai_engine.prophet_forecast_ai import run_price_forecast
    
    st.title("AI Prophet Price Forecast")
    
    df = run_price_forecast()
    
    st.dataframe(df)
    
    st.line_chart(df.set_index("date")["forecast_price"])

# fallback
if __name__ == "__main__":
    render()
