import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")

st.title("🤖 AI Revenue Engine")

# =============================
# PATH
# =============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "bookings.csv")

# =============================
# LOAD DATA
# =============================
if not os.path.exists(DATA_PATH):
    st.error("Dataset non trovato")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])

# =============================
# AI ENGINE (SEMPLICE)
# =============================
def ai_engine(df):
    total_rooms = 100
    df["occupancy"] = df["rooms_sold"] / total_rooms

    last_occ = df["occupancy"].iloc[-1]

    if last_occ > 0.8:
        return "HIGH DEMAND", "Increase price +12%"
    elif last_occ < 0.5:
        return "LOW DEMAND", "Apply discounts"
    else:
        return "NORMAL DEMAND", "Keep price"

# =============================
# UI
# =============================
st.subheader("AI Analysis")

if st.button("Run AI Engine"):
    demand, action = ai_engine(df)

    st.success(f"Demand Level: {demand}")
    st.info(f"Recommended Action: {action}")
