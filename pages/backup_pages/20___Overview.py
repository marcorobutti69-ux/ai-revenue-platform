
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import os
    
    st.set_page_config(layout="wide")
    
    st.title("Overview")
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR,"datasets","hotel_dashboard.csv")
    
    df = pd.read_csv(DATA_PATH)
    
    st.subheader("Bookings Over Time")
    
    fig = px.line(
        df,
        x="date",
        y="bookings",
        title="Bookings Trend"
    )
    
    st.plotly_chart(fig,use_container_width=True)
    
    
    st.subheader("ADR Trend")
    
    fig2 = px.line(
        df,
        x="date",
        y="adr",
        title="Average Daily Rate"
    )
    
    st.plotly_chart(fig2,use_container_width=True)

# fallback
if __name__ == "__main__":
    render()
