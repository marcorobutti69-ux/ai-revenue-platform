
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    
    st.title("Hotel Portfolio Comparison")
    
    st.write("Compare revenue performance across hotels")
    
    data = pd.read_csv("datasets/portfolio_revenue.csv")
    
    data["revenue"] = data["rooms_sold"] * data["avg_price"]
    
    st.subheader("Portfolio Data")
    
    st.dataframe(data)
    
    st.subheader("Revenue by Hotel")
    
    fig = px.bar(
        data,
        x="hotel",
        y="revenue",
        color="hotel",
        title="Revenue Comparison"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Rooms Sold Comparison")
    
    fig2 = px.bar(
        data,
        x="hotel",
        y="rooms_sold",
        color="hotel",
        title="Rooms Sold"
    )
    
    st.plotly_chart(fig2, use_container_width=True)

# fallback
if __name__ == "__main__":
    render()
