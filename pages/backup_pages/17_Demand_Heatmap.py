
import streamlit as st

def render():
    import streamlit as st
    import os
    import pandas as pd
    from analytics.demand_heatmap import DemandHeatmap
    
    st.set_page_config(layout="wide")
    
    st.title("Demand Heatmap")
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR,"datasets","hotel_dashboard.csv")
    
    df = pd.read_csv(DATA_PATH)
    
    heatmap_engine = DemandHeatmap(df)
    
    fig = heatmap_engine.create_heatmap()
    
    st.plotly_chart(fig,use_container_width=True)

# fallback
if __name__ == "__main__":
    render()
