import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")

st.title("🌍 Market Overview")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "competitor_rates.csv")

if not os.path.exists(DATA_PATH):
    st.error("Dataset competitor_rates.csv non trovato")
    st.stop()

df = pd.read_csv(DATA_PATH)

st.subheader("Competitor Prices")

st.dataframe(df)

st.subheader("Market Summary")

st.write(f"Prezzo medio: €{df['price'].mean():.2f}")
st.write(f"Prezzo minimo: €{df['price'].min():.2f}")
st.write(f"Prezzo massimo: €{df['price'].max():.2f}")
