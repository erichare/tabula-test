import tabula
import streamlit as st


def extract_tables(pdf, pages="all"):
    dfs = tabula.read_pdf(pdf, pages=pages)

    return dfs


def st_ui():
    st.title("Tabula Example")
    
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if not uploaded_file:
        uploaded_file = "foo.pdf"
        st.text("Using default file: foo.pdf")

    with st.spinner("Extracting tables..."):
        dfs = extract_tables(uploaded_file, pages="all")

    for df in dfs:
        st.dataframe(df)

if __name__ == "__main__":
    st_ui()
