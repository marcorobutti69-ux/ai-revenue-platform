import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(layout="wide")

st.title("💰 Total Revenue Dashboard")

# =============================
# PATH
# =============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "total_revenue.csv")

# =============================
# LOAD DATA
# =============================
if not os.path.exists(DATA_PATH):
    st.error("File total_revenue.csv non trovato")
    st.stop()

df = pd.read_csv(DATA_PATH)

# =============================
# PREPARAZIONE DATI
# =============================
df["date"] = pd.to_datetime(df["date"])

df["total_revenue"] = df[
    [
        "rooms_revenue",
        "fnb_revenue",
        "spa_revenue",
        "events_revenue",
        "excursions_revenue",
        "transfer_revenue"
    ]
].sum(axis=1)

# =============================
# KPI
# =============================
st.subheader("📊 KPI")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"€{df['total_revenue'].sum():,.0f}")
col2.metric("Avg Daily Revenue", f"€{df['total_revenue'].mean():,.0f}")
col3.metric("Max Daily Revenue", f"€{df['total_revenue'].max():,.0f}")

st.divider()

# =============================
# GRAFICO LINEA
# =============================
st.subheader("📈 Revenue Trend")

fig = px.line(df, x="date", y="total_revenue")
st.plotly_chart(fig, use_container_width=True)

# =============================
# GRAFICO AREA
# =============================
st.subheader("📊 Revenue Breakdown")

fig2 = px.area(
    df,
    x="date",
    y=[
        "rooms_revenue",
        "fnb_revenue",
        "spa_revenue",
        "events_revenue",
        "excursions_revenue",
        "transfer_revenue"
    ]
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# =============================
# TABELLA
# =============================
st.subheader("📋 Dati")

st.dataframe(df)
