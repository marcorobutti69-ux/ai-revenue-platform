
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    from ai_engine.price_calendar_ai import generate_price_calendar
    
    
    st.set_page_config(page_title="AI Price Calendar", layout="wide")
    
    st.title("📅 AI Price Calendar")
    
    st.subheader("Recommended future prices")
    
    
    days = st.slider(
        "Number of days",
        min_value=7,
        max_value=365,
        value=30
    )
    
    
    calendar = generate_price_calendar(days)
    
    df = pd.DataFrame(calendar)
    
    st.dataframe(df, use_container_width=True)
    
    
    st.line_chart(df.set_index("date"))

# fallback
if __name__ == "__main__":
    render()
