import tabula
import os
import subprocess
import streamlit as st

os.environ["JAVA_HOME"] = "/pebble_env/442811d9-1c9e-4230-bd72-9dfe459356d4"


def debug():
    return os.getenv("JAVA_HOME")


def debug2():
    return os.listdir("/")


def extract_tables(pdf, pages="all"):
    dfs = tabula.read_pdf(pdf, pages=pages)

    return dfs


def st_ui():
    st.title("Tabula Example")
    st.text(subprocess.check_output("which java", shell=True).decode("UTF-8"))
    
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
