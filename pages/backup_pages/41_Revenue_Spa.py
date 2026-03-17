
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    st.title("Spa Revenue Dashboard")
    
    data = pd.read_csv("datasets/total_revenue.csv")
    
    spa_revenue = data["spa_revenue"].sum()
    
    st.metric("Total Spa Revenue", spa_revenue)
    
    st.subheader("Spa Revenue Trend")
    
    st.line_chart(data["spa_revenue"])

# fallback
if __name__ == "__main__":
    render()
