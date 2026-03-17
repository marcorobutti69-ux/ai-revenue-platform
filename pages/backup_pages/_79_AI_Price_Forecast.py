
import streamlit as st

def render():
    import streamlit as st
    from ai_engine.forecast_pricing_ai import generate_price_forecast
    
    st.title("AI Price Forecast (30 Days)")
    
    df = generate_price_forecast()
    
    st.dataframe(df)
    
    st.line_chart(df.set_index("date")["forecast_price"])

# fallback
if __name__ == "__main__":
    render()
