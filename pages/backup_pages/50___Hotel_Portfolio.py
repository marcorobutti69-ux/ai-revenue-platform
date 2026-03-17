
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    st.title("Hotel Portfolio Dashboard")
    
    st.write("Manage multiple hotels revenue performance")
    
    # load hotels
    hotels = pd.read_csv("datasets/hotels.csv")
    
    hotel_list = hotels["hotel"].tolist()
    
    selected_hotel = st.selectbox("Select Hotel", hotel_list)
    
    st.subheader("Selected Hotel")
    
    st.write(selected_hotel)
    
    # load bookings
    bookings = pd.read_csv("datasets/bookings.csv")
    
    rooms_sold = bookings["rooms_sold"].sum()
    
    st.subheader("Hotel Performance")
    
    col1, col2 = st.columns(2)
    
    col1.metric("Rooms Sold", rooms_sold)
    
    avg_rooms = bookings["rooms_sold"].mean()
    
    col2.metric("Average Daily Rooms", round(avg_rooms,2))

# fallback
if __name__ == "__main__":
    render()
