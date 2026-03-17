import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(layout="wide")

# =============================
# HEADER
# =============================
st.markdown("""
# 📤 Data Upload Center
### Carica i dati del tuo hotel (Rooms, F&B, Spa, ecc.)
""")

# =============================
# LOGIN CHECK
# =============================
if not st.session_state.get("logged_in"):
    st.warning("⚠️ Effettua il login")
    st.stop()

hotel = st.session_state.get("hotel")

st.success(f"🏨 Hotel attivo: {hotel}")

st.divider()

# =============================
# SELECT REPARTO
# =============================
department = st.selectbox(
    "📊 Seleziona reparto",
    ["rooms", "fnb", "spa", "events", "excursions", "transfers"]
)

st.info("Il file deve avere colonne: date, revenue")

# =============================
# FILE UPLOAD
# =============================
uploaded_file = st.file_uploader(
    "📁 Carica file CSV",
    type=["csv"]
)

# =============================
# PROCESS FILE
# =============================
if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.markdown("### 🔍 Anteprima dati")
        st.dataframe(df.head())

        # =============================
        # VALIDAZIONE
        # =============================
        if "date" not in df.columns or "revenue" not in df.columns:
            st.error("❌ Il file deve contenere colonne: date, revenue")
            st.stop()

        # =============================
        # CONVERSIONE DATA
        # =============================
        df["date"] = pd.to_datetime(df["date"])

        # =============================
        # SAVE BUTTON
        # =============================
        if st.button("💾 Salva nel Database"):

            conn = get_connection()
            cursor = conn.cursor()

            count = 0

            for _, row in df.iterrows():
                cursor.execute("""
                INSERT INTO revenues (date, department, revenue, hotel)
                VALUES (?, ?, ?, ?)
                """, (
                    str(row["date"]),
                    department,
                    float(row["revenue"]),
                    hotel
                ))
                count += 1

            conn.commit()
            conn.close()

            st.success(f"✅ {count} righe caricate con successo!")

    except Exception as e:
        st.error(f"❌ Errore durante il caricamento: {e}")

# =============================
# FOOTER INFO
# =============================
st.divider()

st.markdown("""
### 📌 Formato file richiesto
