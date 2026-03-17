import pdfplumber
import pandas as pd

def load_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    lines = text.split("\n")

    df = pd.DataFrame(lines, columns=["raw_text"])

    return df
