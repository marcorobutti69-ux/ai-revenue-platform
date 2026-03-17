import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")

st.title("🤖 Data & AI Center")

# =============================
# PATH DATA
# =============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "bookings.csv")

# =============================
# LOAD DATA
# =============================
if not os.path.exists(DATA_PATH):
    st.error("Dataset bookings.csv non trovato")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])

# =============================
# AI LOGIC (SEMPLICE)
# =============================
def run_ai_revenue_engine(df):
    total_rooms = 100
    df["occupancy"] = df["rooms_sold"] / total_rooms

    last_occ = df["occupancy"].iloc[-1]

    if last_occ > 0.8:
        return "HIGH DEMAND", "+10% price increase"
    elif last_occ < 0.5:
        return "LOW DEMAND", "Apply discounts"
    else:
        return "NORMAL DEMAND", "Keep current price"

# =============================
# UI
# =============================
st.subheader("Sistema AI")

st.write("✔ Demand Forecast attivo")
st.write("✔ Dynamic Pricing attivo")
st.write("✔ Market Intelligence attivo")

st.divider()

st.subheader("Azioni AI")

# =============================
# BUTTON 1
# =============================
if st.button("Esegui AI Revenue Engine"):
    demand, action = run_ai_revenue_engine(df)

    st.success(f"Domanda: {demand}")
    st.info(f"Azione consigliata: {action}")

# =============================
# BUTTON 2
# =============================
if st.button("Genera Forecast"):
    df["forecast"] = df["rooms_sold"].rolling(3).mean()

    st.write("Forecast ultimi giorni:")
    st.dataframe(df[["date", "rooms_sold", "forecast"]].tail(10))

# =============================
# BUTTON 3
# =============================
if st.button("Analizza mercato"):
    st.success("Market analysis completata (demo)")
