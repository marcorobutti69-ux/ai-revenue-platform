
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    
    st.set_page_config(page_title="GOPPAR", layout="wide")
    
    st.title("📊 GOPPAR Analysis")
    
    st.subheader("Gross Operating Profit Per Available Room")
    
    
    # LOAD DATA
    data = pd.read_csv("datasets/total_revenue.csv")
    
    
    total_revenue = data["rooms_revenue"].sum()
    
    # Example cost assumption
    operating_cost_ratio = 0.65
    
    gross_operating_profit = total_revenue * (1 - operating_cost_ratio)
    
    available_rooms = 100
    
    goppar = gross_operating_profit / available_rooms
    
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Total Rooms Revenue €", int(total_revenue))
    col2.metric("Gross Operating Profit €", int(gross_operating_profit))
    col3.metric("GOPPAR €", round(goppar, 2))

# fallback
if __name__ == "__main__":
    render()
