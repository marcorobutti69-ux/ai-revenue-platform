import streamlit as st
import pandas as pd
import os
import plotly.express as px

from ai_engine.forecast_engine import generate_forecast
from ai_engine.pricing_engine import calculate_price_from_forecast

st.set_page_config(layout="wide")

st.title("💰 AI Pricing + Forecast")

# =============================
# LOAD DATA
# =============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "bookings.csv")

if not os.path.exists(DATA_PATH):
    st.error("Dataset non trovato")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])

# =============================
# GENERA FORECAST
# =============================
forecast_df = generate_forecast(df, days=7)

# =============================
# PARAMETRI
# =============================
st.subheader("Parametri")

base_price = st.slider("Base Price (€)", 50, 300, 120)
total_rooms = st.slider("Total Rooms", 50, 200, 100)

# =============================
# CALCOLO PREZZI FUTURI
# =============================
prices = []
occupancies = []

for forecast_rooms in forecast_df["forecast_rooms"]:
    price, occ = calculate_price_from_forecast(
        forecast_rooms,
        total_rooms,
        base_price
    )
    prices.append(price)
    occupancies.append(occ)

forecast_df["recommended_price"] = prices
forecast_df["occupancy"] = occupancies

# =============================
# GRAFICO
# =============================
st.subheader("📈 Future Pricing Strategy")

fig = px.line(forecast_df, x="date", y="recommended_price",
              title="Recommended Prices (Next 7 Days)")

st.plotly_chart(fig, use_container_width=True)

# =============================
# TABELLA
# =============================
st.subheader("📋 Pricing Table")

st.dataframe(forecast_df)

# =============================
# INSIGHT AI
# =============================
st.subheader("🧠 AI Strategy")

avg_occ = sum(occupancies) / len(occupancies)

if avg_occ > 0.8:
    st.success("High future demand → Increase prices aggressively")
elif avg_occ < 0.5:
    st.warning("Low future demand → Apply promotions")
else:
    st.info("Stable demand → Maintain pricing")
