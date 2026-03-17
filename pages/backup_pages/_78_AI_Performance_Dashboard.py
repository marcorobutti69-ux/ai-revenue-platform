
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    st.title("AI Performance Dashboard")
    
    # CARICA DATI
    df = pd.read_csv("datasets/price_recommendations.csv")
    
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    
    # KPI
    latest = df.iloc[-1]
    
    st.subheader("Latest AI Decision")
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Recommended Price", latest["recommended_price"])
    col2.metric("Market Avg", latest["market_avg"])
    col3.metric("Demand Index", latest["demand_index"])
    
    # ALERT
    st.subheader("AI Alerts")
    
    if "alerts" in df.columns:
        st.write(latest["alerts"])
    
    # GRAFICO PREZZI
    st.subheader("Price Trend")
    
    st.line_chart(df.set_index("date")["recommended_price"])
    
    # CONFRONTO MERCATO
    st.subheader("AI vs Market")
    
    df_plot = df.set_index("date")[["recommended_price", "market_avg"]]
    
    st.line_chart(df_plot)
    
    # STRATEGIA
    st.subheader("AI Strategy")
    
    if latest["recommended_price"] < latest["market_avg"]:
        st.info("Competitive pricing strategy")
    
    elif latest["recommended_price"] > latest["market_avg"]:
        st.warning("Premium pricing strategy")
    
    else:
        st.success("Aligned with market")

# fallback
if __name__ == "__main__":
    render()
