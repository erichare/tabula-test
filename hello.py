import tabula
import streamlit as st

def main():
    st.title("PDF table extraction with Tabula")
    
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    file_name = uploaded_file.name

    with st.spinner("Extracting with Tabula..."):
        dfs = tabula.read_pdf(uploaded_file, pages='all')

    for df in dfs:
        st.dataframe(df)

if __name__ == "__main__":
    main()
