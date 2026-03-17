import streamlit as st
import pandas as pd
import os
import plotly.express as px

from ai_engine.forecast_engine import generate_forecast

st.set_page_config(layout="wide")

st.title("📈 Demand Forecast AI")

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
# GRAFICO STORICO + FUTURO
# =============================
st.subheader("Demand Forecast (Next 7 Days)")

fig = px.line(df, x="date", y="rooms_sold", title="Historical Demand")
fig.add_scatter(
    x=forecast_df["date"],
    y=forecast_df["forecast_rooms"],
    mode="lines",
    name="Forecast",
    line=dict(dash="dash")
)

st.plotly_chart(fig, use_container_width=True)

# =============================
# TABELLA
# =============================
st.subheader("Forecast Table")

st.dataframe(forecast_df)
