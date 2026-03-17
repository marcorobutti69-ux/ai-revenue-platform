
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.revenue_kpi_ai import calculate_revenue_kpi
    
    
    st.set_page_config(page_title="AI Revenue KPI", layout="wide")
    
    st.title("📊 AI Revenue KPI")
    
    data = calculate_revenue_kpi()
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Occupancy %", data["occupancy"])
    col2.metric("ADR €", data["adr"])
    col3.metric("RevPAR €", data["revpar"])

# fallback
if __name__ == "__main__":
    render()
