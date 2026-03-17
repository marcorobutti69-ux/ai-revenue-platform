
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    st.title("Events Revenue Dashboard")
    
    data = pd.read_csv("datasets/total_revenue.csv")
    
    events_revenue = data["events_revenue"].sum()
    
    st.metric("Total Events Revenue", events_revenue)
    
    st.subheader("Events Revenue Trend")
    
    st.line_chart(data["events_revenue"])

# fallback
if __name__ == "__main__":
    render()
