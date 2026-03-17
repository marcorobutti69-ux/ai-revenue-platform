import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="AI Revenue Platform", layout="wide")

def get_connection():
    return sqlite3.connect("../hotel_ai.db")

@st.cache_data
def load_data():
    conn = get_connection()
    try:
        df = pd.read_sql_query("SELECT * FROM bookings", conn)
    except:
        df = pd.DataFrame(columns=["date", "rooms_sold"])
    conn.close()
    return df

df = load_data()

if df.empty:
    st.warning("Modalità demo attiva")

    df = pd.DataFrame({
        "date": pd.date_range(start="2026-01-01", periods=10),
        "rooms_sold": [40, 55, 60, 70, 65, 80, 75, 60, 50, 45]
    })

st.title("AI Hotel Revenue Platform")
st.caption("Dashboard Overview")

if not df.empty and "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])

rooms_available = 100

if not df.empty:
    total_rooms_sold = df["rooms_sold"].sum()
    occupancy = total_rooms_sold / (rooms_available * len(df))
    adr = df["rooms_sold"].mean()
    revpar = adr * occupancy
else:
    occupancy = 0
    adr = 0
    revpar = 0

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Occupancy", f"{occupancy:.2%}")
col2.metric("ADR", f"€ {adr:.2f}")
col3.metric("RevPAR", f"€ {revpar:.2f}")

st.subheader("Booking Trend")

if not df.empty:
    fig = px.line(df, x="date", y="rooms_sold")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No booking data available")

st.subheader("AI Insight")

if not df.empty:
    avg_demand = df["rooms_sold"].mean()
    if avg_demand > 60:
        st.success("High demand → increase price")
    elif avg_demand < 40:
        st.warning("Low demand → promotions needed")
    else:
        st.info("Demand stable")
else:
    st.info("No data for AI")

st.divider()
st.caption("AI Revenue Platform v8.0")
