
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    from data_loader.excel_loader import load_excel
    from data_loader.pdf_loader import load_pdf
    from data_loader.word_loader import load_word
    
    
    st.title("Hotel Data Import Center")
    
    st.write("Upload hotel files (Excel, PDF, Word)")
    
    
    file = st.file_uploader("Upload file")
    
    
    data_type = st.selectbox(
        "Select Data Type",
        [
            "Rooms",
            "F&B",
            "Spa",
            "Excursions",
            "Transfers",
            "Bookings"
        ]
    )
    
    
    if file:
    
        if file.name.endswith(".xlsx"):
    
            df = load_excel(file)
    
        elif file.name.endswith(".pdf"):
    
            df = load_pdf(file)
    
        elif file.name.endswith(".docx"):
    
            df = load_word(file)
    
        else:
    
            st.error("Unsupported file type")
    
            df = None
    
    
        if df is not None:
    
            st.write("Data preview")
    
            st.dataframe(df)
    
    
            if st.button("Save Dataset"):
    
                path = f"datasets/{data_type.lower()}_data.csv"
    
                df.to_csv(path, index=False)
    
                st.success(f"Dataset saved to {path}")

# fallback
if __name__ == "__main__":
    render()
