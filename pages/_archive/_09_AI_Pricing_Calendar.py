
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    from ai_engine.dynamic_pricing_calendar_ai import generate_pricing_calendar
    
    
    st.set_page_config(page_title="AI Pricing Calendar", layout="wide")
    
    st.title("📅 AI Dynamic Pricing Calendar")
    
    calendar = generate_pricing_calendar()
    
    df = pd.DataFrame(calendar)
    
    st.dataframe(df, use_container_width=True)

# fallback
if __name__ == "__main__":
    render()
