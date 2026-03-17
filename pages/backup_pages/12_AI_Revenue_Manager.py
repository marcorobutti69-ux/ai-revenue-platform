
import streamlit as st

def render():
    import streamlit as st
    
    from ai_engine.automatic_pricing_engine import automatic_price
    
    
    st.set_page_config(page_title="AI Revenue Manager", layout="wide")
    
    st.title("AI Revenue Manager")
    
    st.subheader("Automatic revenue optimization engine")
    
    
    current_price = st.number_input(
        "Current Room Price",
        min_value=50,
        max_value=1000,
        value=120
    )
    
    
    if st.button("Run AI Pricing"):
    
        new_price = automatic_price(
            current_price,
            "datasets/competitor_rates.csv",
            "datasets/bookings.csv"
        )
    
        st.success(f"Recommended Price: € {new_price}")

# fallback
if __name__ == "__main__":
    render()
