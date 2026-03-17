import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(layout="wide")

# =============================
# DATABASE CONNECTION
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

    # UTENTE DEMO
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

# =============================
# APP ACCESSO
# =============================
if st.session_state.get("logged_in"):
    st.sidebar.success(f"🏨 Hotel: {st.session_state['hotel']}")
    st.write("Usa il menu a sinistra per navigare tra le sezioni")
