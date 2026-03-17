
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    import os
    
    
    st.title("Market Intelligence")
    
    dataset_path = "datasets/competitor_rates.csv"
    
    
    # ---------------------------------------------------
    # CREATE DATASET IF NOT EXISTS
    # ---------------------------------------------------
    
    if not os.path.exists(dataset_path):
    
        df_init = pd.DataFrame({
            "hotel": ["Hotel A", "Hotel B", "Hotel C", "Hotel D"],
            "price": [140, 155, 160, 150]
        })
    
        df_init.to_csv(dataset_path, index=False)
    
    
    # ---------------------------------------------------
    # LOAD DATA
    # ---------------------------------------------------
    
    df = pd.read_csv(dataset_path)
    
    
    # ---------------------------------------------------
    # CALCULATE MARKET METRICS
    # ---------------------------------------------------
    
    market_avg = df["price"].mean()
    
    min_price = df["price"].min()
    
    max_price = df["price"].max()
    
    
    # ---------------------------------------------------
    # DISPLAY METRICS
    # ---------------------------------------------------
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Market Average Price", round(market_avg,2))
    
    col2.metric("Lowest Competitor Price", round(min_price,2))
    
    col3.metric("Highest Competitor Price", round(max_price,2))
    
    
    # ---------------------------------------------------
    # AI MARKET STRATEGY
    # ---------------------------------------------------
    
    st.subheader("AI Market Strategy")
    
    if market_avg > 155:
    
        st.success("Market price high → opportunity to increase rates")
    
    elif market_avg < 135:
    
        st.warning("Market price low → consider promotions")
    
    else:
    
        st.info("Market stable → maintain pricing")
    
    
    # ---------------------------------------------------
    # SHOW TABLE
    # ---------------------------------------------------
    
    st.subheader("Competitor Rates")
    
    st.dataframe(df)

# fallback
if __name__ == "__main__":
    render()
