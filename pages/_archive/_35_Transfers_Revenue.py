
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    st.title("Transfers Revenue Dashboard")
    
    data = pd.read_csv("datasets/total_revenue.csv")
    
    transfer_revenue = data["transfer_revenue"].sum()
    
    st.metric("Total Transfers Revenue", transfer_revenue)
    
    st.line_chart(data["transfer_revenue"])

# fallback
if __name__ == "__main__":
    render()
