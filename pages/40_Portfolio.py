import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🏨 Hotel Portfolio")

# =============================
# DATI DEMO
# =============================
data = {
    "Hotel": ["Milano", "Roma", "Venezia", "Firenze"],
    "Revenue": [120000, 95000, 110000, 87000],
    "Occupancy": [78, 72, 85, 69]
}

df = pd.DataFrame(data)

# =============================
# KPI
# =============================
st.subheader("📊 Portfolio KPI")

col1, col2 = st.columns(2)

col1.metric("Total Revenue", f"€{df['Revenue'].sum():,}")
col2.metric("Avg Occupancy", f"{df['Occupancy'].mean():.1f}%")

# =============================
# TABELLA
# =============================
st.subheader("🏨 Hotels")

st.dataframe(df)
