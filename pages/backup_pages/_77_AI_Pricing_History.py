
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    st.title("AI Pricing History")
    
    df = pd.read_csv("datasets/price_recommendations.csv")
    
    st.dataframe(df)
    
    st.line_chart(df.set_index("date")["recommended_price"])

# fallback
if __name__ == "__main__":
    render()
