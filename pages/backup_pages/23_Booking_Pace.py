
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import os
    import sys
    
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    
    from main.booking_pace_forecast import BookingPaceForecast
    
    st.set_page_config(layout="wide")
    
    st.title("Booking Pace Analysis")
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR,"datasets","booking_pace.csv")
    
    engine = BookingPaceForecast(DATA_PATH)
    
    pace = engine.booking_pace()
    
    st.subheader("Booking Pace Table")
    
    st.dataframe(pace,use_container_width=True)
    
    st.subheader("Booking Pace Trend")
    
    fig = px.bar(
        pace,
        x="arrival_date",
        y="bookings",
        title="Bookings by Arrival Date"
    )
    
    st.plotly_chart(fig,use_container_width=True)

# fallback
if __name__ == "__main__":
    render()
