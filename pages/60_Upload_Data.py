import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(layout="wide")

st.title("📤 Smart Data Upload V2")

# =============================
# LOGIN CHECK
# =============================
if not st.session_state.get("logged_in"):
    st.warning("⚠️ Effettua il login")
    st.stop()

hotel = st.session_state.get("hotel")

st.success(f"🏨 Hotel: {hotel}")

st.divider()

# =============================
# DEPARTMENT
# =============================
department = st.selectbox(
    "Seleziona reparto",
    ["rooms", "fnb", "spa", "events", "excursions", "transfers"]
)

# =============================
# FILE UPLOAD
# =============================
uploaded_file = st.file_uploader(
    "Carica file (CSV o Excel)",
    type=["csv", "xlsx"]
)

# =============================
# SMART COLUMN DETECTION
# =============================
def detect_columns(df):
    date_col = None
    revenue_col = None

    for col in df.columns:
        col_lower = col.lower()

        if any(x in col_lower for x in ["date", "data", "giorno"]):
            date_col = col

        if any(x in col_lower for x in ["revenue", "amount", "totale", "incasso", "sales"]):
            revenue_col = col

    return date_col, revenue_col

# =============================
# PROCESS FILE
# =============================
if uploaded_file:

    try:
        # READ FILE
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.subheader("Anteprima dati")
        st.dataframe(df.head())

        # DETECT COLUMNS
        date_col, revenue_col = detect_columns(df)

        if not date_col or not revenue_col:
            st.error("❌ Impossibile riconoscere colonne automaticamente")
            st.write("Colonne trovate:", df.columns.tolist())
            st.stop()

        st.success(f"✔ Colonna data: {date_col}")
        st.success(f"✔ Colonna revenue: {revenue_col}")

        # NORMALIZE
        df_clean = pd.DataFrame()
        df_clean["date"] = pd.to_datetime(df[date_col])
        df_clean["revenue"] = pd.to_numeric(df[revenue_col], errors="coerce")

        df_clean = df_clean.dropna()

        st.subheader("Dati normalizzati")
        st.dataframe(df_clean.head())

        # SAVE
        if st.button("💾 Salva nel database"):

            conn = get_connection()
            cursor = conn.cursor()

            count = 0

            for _, row in df_clean.iterrows():
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

            st.success(f"✅ {count} righe caricate!")

    except Exception as e:
        st.error(f"Errore: {e}")

# =============================
# INFO
# =============================
st.divider()

st.markdown("""
### 💡 Supportato:

- CSV ✔  
- Excel (.xlsx) ✔  
- Colonne automatiche ✔  

### 🚫 Non ancora:

- PDF  
- Word  
- ODT  
""")
