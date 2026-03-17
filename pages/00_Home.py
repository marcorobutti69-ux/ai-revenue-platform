import streamlit as st
import pandas as pd
import plotly.express as px

import sqlite3

def get_connection():
    return sqlite3.connect("../hotel_ai.db")  # percorso relativo corretto

st.set_page_config(layout="wide")

# =============================
# HEADER
# =============================
st.markdown("""
# 🧠 AI Revenue Control Tower
### Real-time Revenue Intelligence Platform
""")

# =============================
# LOGIN CHECK
# =============================
if not st.session_state.get("logged_in"):
    st.warning("⚠️ Effettua il login")
    st.stop()

hotel = st.session_state.get("hotel")

# =============================
# LOAD DATA
# =============================
conn = get_connection()

query = f"""
SELECT date, rooms_sold
FROM bookings
WHERE hotel = '{hotel}'
"""

df = pd.read_sql(query, conn)
conn.close()

if df.empty:
    st.error("❌ Nessun dato disponibile")
    st.stop()

df["date"] = pd.to_datetime(df["date"])

# =============================
# KPI CALCOLI
# =============================
total_rooms = 100
df["occupancy"] = df["rooms_sold"] / total_rooms

adr = 120
df["revpar"] = df["occupancy"] * adr

# =============================
# KPI CARDS (ENTERPRISE)
# =============================
st.markdown("## 📊 Performance Overview")

col1, col2, col3, col4 = st.columns(4)

def card(title, value):
    st.markdown(f"""
    <div style="
        background-color:#1C1F26;
        padding:20px;
        border-radius:15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
        text-align:center;">
        <h4 style="color:#aaa;">{title}</h4>
        <h2 style="color:white;">{value}</h2>
    </div>
    """, unsafe_allow_html=True)

with col1:
    card("Occupancy", f"{df['occupancy'].mean()*100:.1f}%")

with col2:
    card("ADR", f"€{adr}")

with col3:
    card("RevPAR", f"€{df['revpar'].mean():.2f}")

with col4:
    card("Revenue", f"€{(df['rooms_sold']*adr).sum():,.0f}")

st.divider()

# =============================
# GRAFICO DEMAND
# =============================
st.markdown("## 📈 Demand Trend")

fig = px.line(
    df,
    x="date",
    y="rooms_sold",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# =============================
# AI INSIGHTS
# =============================
st.markdown("## 🧠 AI Insights")

last_occ = df["occupancy"].iloc[-1]

if last_occ > 0.8:
    st.markdown("🟢 **High Demand Detected → Increase Prices**")
elif last_occ < 0.5:
    st.markdown("🔴 **Low Demand → Activate Promotions**")
else:
    st.markdown("🟡 **Stable Market Conditions**")

st.divider()

# =============================
# QUICK ACTIONS
# =============================
st.markdown("## ⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

if col1.button("Run Pricing AI"):
    st.success("Pricing aggiornato")

if col2.button("Generate Forecast"):
    st.success("Forecast generato")

if col3.button("Market Analysis"):
    st.success("Analisi completata")
