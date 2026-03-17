
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    st.title("Excursions Revenue Dashboard")
    
    data = pd.read_csv("datasets/total_revenue.csv")
    
    exc_revenue = data["excursions_revenue"].sum()
    
    st.metric("Total Excursions Revenue", exc_revenue)
    
    st.line_chart(data["excursions_revenue"])

# fallback
if __name__ == "__main__":
    render()
