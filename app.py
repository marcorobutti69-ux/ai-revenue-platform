import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(layout="wide")

# =============================
# DATABASE CONNECTION + INIT
# =============================
def get_connection():
    return sqlite3.connect("hotel_ai.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        password TEXT,
        hotel TEXT
    )
    """)

    # BOOKINGS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        date TEXT,
        rooms_sold INTEGER,
        hotel TEXT
    )
    """)

    # REVENUES TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS revenues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        department TEXT,
        revenue REAL,
        hotel TEXT
    )
    """)

    # Inserisce utente demo se tabella vuota
    cursor.execute("SELECT * FROM users")
    if not cursor.fetchall():
        cursor.execute("""
        INSERT INTO users (username, password, hotel)
        VALUES ('admin', 'admin123', 'Hotel Demo')
        """)

    conn.commit()
    conn.close()

# inizializza DB
init_db()

# =============================
# LOGIN
# =============================
st.sidebar.title("🏨 AI Revenue Platform")
st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    try:
        conn = get_connection()
        query = f"""
        SELECT * FROM users
        WHERE username = '{username}' AND password = '{password}'
        """
        user = pd.read_sql(query, conn)
        conn.close()

        if not user.empty:
            st.session_state["logged_in"] = True
            st.session_state["hotel"] = user.iloc[0]["hotel"]
            st.success(f"Benvenuto {username}")
        else:
            st.error("Credenziali errate")
    except Exception as e:
        st.error(f"Errore database: {e}")

# blocca accesso se non loggato
if not st.session_state.get("logged_in"):
    st.stop()

hotel = st.session_state.get("hotel", "Hotel Demo")
st.sidebar.success(f"🏨 Hotel attivo: {hotel}")

# =============================
# CARICAMENTO DATI BOOKINGS
# =============================
try:
    conn = get_connection()
    query = f"""
    SELECT date, rooms_sold
    FROM bookings
    WHERE hotel = '{hotel}'
    """
    df = pd.read_sql(query, conn)
    conn.close()
except Exception as e:
    st.error(f"Errore database: {e}")
    st.stop()

if df.empty:
    st.error("❌ Nessun dato trovato per questo hotel")
    st.stop()

df["date"] = pd.to_datetime(df["date"])

# =============================
# KPI CALC
# =============================
total_rooms = 100
df["occupancy"] = df["rooms_sold"] / total_rooms
adr = 120
df["revpar"] = df["occupancy"] * adr

st.markdown("## 📊 Performance Overview")
col1, col2, col3, col4 = st.columns(4)

def card(title, value):
    st.markdown(f"""
    <div style="
        background-color:#1C1F26;
        padding:20px;
        border-radius:15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
        text-align:center;">
        <h4 style="color:#aaa;">{title}</h4>
        <h2 style="color:white;">{value}</h2>
    </div>
    """, unsafe_allow_html=True)

with col1:
    card("Occupancy", f"{df['occupancy'].mean()*100:.1f}%")
with col2:
    card("ADR", f"€{adr}")
with col3:
    card("RevPAR", f"€{df['revpar'].mean():.2f}")
with col4:
    card("Revenue", f"€{(df['rooms_sold']*adr).sum():,.0f}")

st.divider()

# =============================
# GRAFICO DEMAND
# =============================
fig = px.line(
    df,
    x="date",
    y="rooms_sold",
    template="plotly_dark",
    title="📈 Demand Trend"
)
st.plotly_chart(fig, use_container_width=True)

# =============================
# AI INSIGHTS
# =============================
st.markdown("## 🧠 AI Insights")
last_occ = df["occupancy"].iloc[-1]

if last_occ > 0.8:
    st.markdown("🟢 **High Demand Detected → Increase Prices**")
elif last_occ < 0.5:
    st.markdown("🔴 **Low Demand → Activate Promotions**")
else:
    st.markdown("🟡 **Stable Market Conditions**")

st.divider()

# =============================
# QUICK ACTIONS
# =============================
st.markdown("## ⚡ Quick Actions")
col1, col2, col3 = st.columns(3)

if col1.button("Run Pricing AI"):
    st.success("Pricing aggiornato")

if col2.button("Generate Forecast"):
    st.success("Forecast generato")

if col3.button("Market Analysis"):
    st.success("Analisi completata")
