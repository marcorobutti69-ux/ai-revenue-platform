import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(layout="wide")

# =============================
# SIDEBAR
# =============================
st.sidebar.markdown("## 🧠 AI Revenue Platform")
st.sidebar.markdown("---")

# =============================
# LOGIN
# =============================
st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    conn = get_connection()

    query = f"""
    SELECT * FROM users
    WHERE username = '{username}'
    AND password = '{password}'
    """

    user = pd.read_sql(query, conn)
    conn.close()

    if not user.empty:
        st.session_state["logged_in"] = True
        st.session_state["hotel"] = user.iloc[0]["hotel"]
        st.success(f"Benvenuto {username}")
    else:
        st.error("Credenziali errate")

# =============================
# APP ACCESSO
# =============================
if st.session_state.get("logged_in"):
    st.sidebar.success(f"🏨 {st.session_state['hotel']}")
    st.write("Usa il menu a sinistra")
