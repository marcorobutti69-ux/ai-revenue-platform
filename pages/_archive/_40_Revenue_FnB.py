
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    st.title("F&B Revenue Dashboard")
    
    data = pd.read_csv("datasets/total_revenue.csv")
    
    fnb_revenue = data["fnb_revenue"].sum()
    
    st.metric("Total F&B Revenue", fnb_revenue)
    
    st.subheader("F&B Revenue Trend")
    
    st.line_chart(data["fnb_revenue"])

# fallback
if __name__ == "__main__":
    render()
