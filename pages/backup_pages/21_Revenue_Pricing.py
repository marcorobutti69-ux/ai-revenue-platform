
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.automatic_pricing_engine import automatic_price
    
    
    st.set_page_config(page_title="Pricing Engine", layout="wide")
    
    st.title("💰 Pricing Engine")
    
    st.subheader("AI Dynamic Pricing")
    
    
    current_price = st.number_input(
        "Current Room Price",
        min_value=50,
        max_value=1000,
        value=120
    )
    
    
    if st.button("Calculate AI Price"):
    
        recommended_price = automatic_price(
            current_price,
            "datasets/competitor_rates.csv",
            "datasets/bookings.csv"
        )
    
        st.success(f"Recommended Price: € {recommended_price}")

# fallback
if __name__ == "__main__":
    render()
