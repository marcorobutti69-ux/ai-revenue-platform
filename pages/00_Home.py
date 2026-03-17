import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(
    page_title="AI Revenue Platform",
    layout="wide"
)

# -------------------------------
# DATABASE
# -------------------------------
def get_connection():
    try:
        return sqlite3.connect("hotel_ai.db")
    except:
        return None

# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data():
    conn = get_connection()

    if conn is None:
        return pd.DataFrame()

    try:
        df = pd.read_sql_query("SELECT * FROM bookings", conn)
    except:
        df = pd.DataFrame()

    conn.close()
    return df

df = load_data()

# -------------------------------
# DEMO MODE (IMPORTANTISSIMO)
# -------------------------------
if df.empty:
    st.warning("⚠️ Modalità demo attiva (nessun dato reale trovato)")

    df = pd.DataFrame({
        "date": pd.date_range(start="2026-01-01", periods=10),
        "rooms_sold": [40, 55, 60, 70, 65, 80, 75, 60, 50, 45]
    })

# -------------------------------
# TITLE
# -------------------------------
st.title("🏨 AI Hotel Revenue Platform")
st.caption("Dashboard Overview")

# -------------------------------
# DATA PREP
# -------------------------------
df["date"] = pd.to_datetime(df["date"])

rooms_available = 100

total_rooms_sold = df["rooms_sold"].sum()
occupancy = total_rooms_sold / (rooms_available * len(df))
adr = df["rooms_sold"].mean()
revpar = adr * occupancy

# -------------------------------
# KPI
# -------------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Occupancy", f"{occupancy:.2%}")
col2.metric("ADR", f"€ {adr:.2f}")
col3.metric("RevPAR", f"€ {revpar:.2f}")

# -------------------------------
# CHART
# -------------------------------
st.subheader("📈 Booking Trend")

fig = px.line(
    df,
    x="date",
    y="rooms_sold",
    title="Rooms Sold Over Time"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# AI INSIGHT
# -------------------------------
st.subheader("🧠 AI Insight")

avg_demand = df["rooms_sold"].mean()

if avg_demand > 60:
    st.success("🔥 Alta domanda → aumenta i prezzi")
elif avg_demand < 40:
    st.warning("📉 Bassa domanda → attiva promozioni")
else:
    st.info("📊 Domanda stabile")

# -------------------------------
# FOOTER
# -------------------------------
st.divider()
st.caption("AI Revenue Management System • v8.0")
