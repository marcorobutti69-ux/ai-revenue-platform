from docx import Document
import pandas as pd

def load_word(file):

    doc = Document(file)

    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    df = pd.DataFrame(text, columns=["raw_text"])

    return df
