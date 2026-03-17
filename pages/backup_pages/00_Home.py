import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =============================
# CONFIG PAGINA
# =============================
st.set_page_config(page_title="AI Revenue Command Center", layout="wide")

st.title("🤖 AI Revenue Command Center")

# =============================
# PATH DATASET SICURO (FIX DEFINITIVO)
# =============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "bookings.csv")

# =============================
# LOAD DATA SICURO
# =============================
if not os.path.exists(DATA_PATH):
    st.error("❌ ERRORE: bookings.csv NON TROVATO in /datasets")
    st.stop()

try:
    df = pd.read_csv(DATA_PATH)
except Exception as e:
    st.error(f"Errore lettura dataset: {e}")
    st.stop()

# =============================
# VALIDAZIONE DATI
# =============================
if "date" not in df.columns or "rooms_sold" not in df.columns:
    st.error("❌ bookings.csv deve contenere colonne: date, rooms_sold")
    st.stop()

# =============================
# PREPARAZIONE DATI
# =============================
df["date"] = pd.to_datetime(df["date"])

total_rooms = 100

df["occupancy"] = df["rooms_sold"] / total_rooms
df["adr"] = 120  # placeholder (poi collegheremo AI)
df["revpar"] = df["adr"] * df["occupancy"]

# KPI
adr = df["adr"].mean()
revpar = df["revpar"].mean()
occupancy = df["occupancy"].mean() * 100
revenue = (df["rooms_sold"] * df["adr"]).sum()

# =============================
# KPI TOP
# =============================
st.subheader("📊 KPI Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("ADR", f"€{adr:.2f}")
col2.metric("RevPAR", f"€{revpar:.2f}")
col3.metric("Occupancy", f"{occupancy:.1f}%")
col4.metric("Revenue", f"€{revenue:,.0f}")

st.divider()

# =============================
# GRAFICI
# =============================
st.subheader("📈 Performance")

col1, col2 = st.columns(2)

fig1 = px.line(df, x="date", y="rooms_sold", title="Booking Trend")
col1.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(df, x="date", y="occupancy", title="Occupancy Trend")
col2.plotly_chart(fig2, use_container_width=True)

st.divider()

# =============================
# AI INSIGHTS
# =============================
st.subheader("🧠 AI Insights")

last_occupancy = df["occupancy"].iloc[-1]

if last_occupancy > 0.8:
    st.success("High demand detected → Increase price by +10%")
elif last_occupancy < 0.5:
    st.warning("Low demand → Consider promotions")
else:
    st.info("Stable demand → Keep current pricing")

# =============================
# ALERT
# =============================
st.subheader("🚨 Alerts")

recent_avg = df["rooms_sold"].tail(7).mean()

if recent_avg < 40:
    st.error("Low booking pace next 7 days")
else:
    st.success("Booking pace is healthy")

st.divider()

# =============================
# DATA TABLE
# =============================
st.subheader("📋 Latest Data")

st.dataframe(df.tail(10))
