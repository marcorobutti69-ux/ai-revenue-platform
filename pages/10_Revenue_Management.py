import streamlit as st

st.set_page_config(layout="wide")

st.title("💼 Revenue Management Control")

st.subheader("📊 Seleziona modulo")

col1, col2, col3 = st.columns(3)

# =============================
# BUTTONS NAVIGATION
# =============================
if col1.button("📊 Revenue Overview"):
    st.switch_page("pages/10_Revenue_Overview.py")

if col2.button("💰 Pricing"):
    st.switch_page("pages/11_Revenue_Pricing.py")

if col3.button("📈 KPI & Forecast"):
    st.switch_page("pages/12_Revenue_KPI.py")

st.divider()

# =============================
# QUICK SUMMARY
# =============================
st.subheader("🧠 AI Quick Summary")

st.info("""
Questa sezione permette di:

- Analizzare performance revenue
- Ottimizzare pricing dinamico
- Visualizzare forecast domanda
""")
