import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")

st.title("📊 Revenue Overview")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "bookings.csv")

if not os.path.exists(DATA_PATH):
    st.error("Dataset bookings.csv non trovato")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])

total_rooms = 100
df["occupancy"] = df["rooms_sold"] / total_rooms

st.subheader("KPI")

col1, col2 = st.columns(2)
col1.metric("Rooms Sold", int(df["rooms_sold"].sum()))
col2.metric("Occupancy", f"{df['occupancy'].mean()*100:.1f}%")

st.subheader("Dati")
st.dataframe(df.tail(20))
