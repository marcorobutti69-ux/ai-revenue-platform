
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    import altair as alt
    
    from ai_engine.portfolio_ai import analyze_portfolio
    
    
    st.set_page_config(page_title="AI Portfolio Intelligence", layout="wide")
    
    st.title("🏨 AI Portfolio Intelligence")
    
    
    # ==============================
    # SUMMARY DATA
    # ==============================
    
    data = analyze_portfolio()
    
    col1, col2 = st.columns(2)
    
    col1.metric("Total Portfolio Revenue €", int(data["total_revenue"]))
    col2.metric("Average Hotel Revenue €", int(data["average_revenue"]))
    
    st.write("Best Performing Hotel:", data["best_hotel"])
    st.write("Lowest Performing Hotel:", data["worst_hotel"])
    
    
    st.divider()
    
    
    # ==============================
    # LOAD PORTFOLIO DATA
    # ==============================
    
    portfolio = pd.read_csv("datasets/portfolio_revenue.csv")
    
    # calcolo revenue
    portfolio["revenue"] = portfolio["rooms_sold"] * portfolio["avg_price"]
    
    
    # ==============================
    # CHART
    # ==============================
    
    st.subheader("Revenue by Hotel")
    
    chart = alt.Chart(portfolio).mark_bar().encode(
        x="hotel:N",
        y="revenue:Q",
        tooltip=["hotel", "revenue"]
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    
    # ==============================
    # TABLE
    # ==============================
    
    st.subheader("Portfolio Data")
    
    st.dataframe(portfolio)

# fallback
if __name__ == "__main__":
    render()
