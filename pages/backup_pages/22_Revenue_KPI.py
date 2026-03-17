
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    import os
    import plotly.express as px
    
    st.set_page_config(layout="wide")
    
    st.title("Revenue KPIs")
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR,"datasets","hotel_dashboard.csv")
    
    df = pd.read_csv(DATA_PATH)
    
    total_revenue = df["room_revenue"].sum()
    total_bookings = df["bookings"].sum()
    adr = round(df["adr"].mean(),2)
    
    rooms_available = 200
    revpar = round(total_revenue / (rooms_available * len(df)),2)
    
    col1,col2,col3,col4 = st.columns(4)
    
    col1.metric("Total Revenue",total_revenue)
    col2.metric("Bookings",total_bookings)
    col3.metric("ADR",adr)
    col4.metric("RevPAR",revpar)
    
    st.subheader("Revenue Trend")
    
    fig = px.line(
        df,
        x="date",
        y="room_revenue",
        title="Room Revenue Over Time"
    )
    
    st.plotly_chart(fig,use_container_width=True)

# fallback
if __name__ == "__main__":
    render()
