
import streamlit as st

def render():
    import streamlit as st
    import pandas as pd
    
    from data_loader.excel_loader import load_excel
    from data_loader.pdf_loader import load_pdf
    from data_loader.word_loader import load_word
    
    st.title("AI Document Read Center")
    
    st.write("Upload hotel documents and convert them into datasets")
    
    
    file = st.file_uploader("Upload document")
    
    
    data_type = st.selectbox(
        "Select document type",
        [
            "Rooms",
            "F&B",
            "Spa",
            "Excursions",
            "Transfers"
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
    
            st.subheader("Document Preview")
    
            st.dataframe(df)
    
    
            if st.button("Convert to Dataset"):
    
                path = f"datasets/{data_type.lower()}_data.csv"
    
                df.to_csv(path, index=False)
    
                st.success(f"Dataset created: {path}")

# fallback
if __name__ == "__main__":
    render()
