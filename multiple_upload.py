import streamlit as st
import pandas as pd

images = st.file_uploader("Upload Images", type=["jpg", "png"], accept_multiple_files=True)

for img in images:
    st.image(img, caption=img.name, width=300)

files = st.file_uploader("Upload CSV files", type="csv", accept_multiple_files=True)

for file in files:
    df = pd.read_csv(file)
    st.write("File Name:", file.name)
    st.dataframe(df)

files1 = st.file_uploader("Upload Excel files", type=["xlsx"], accept_multiple_files=True)

for file1 in files1:
    df = pd.read_excel(file1)
    st.write("Uploaded:", file1.name)
    st.dataframe(df)

files2 = st.file_uploader("Upload files", accept_multiple_files=True)

for file2 in files2:
    st.write("File:", file2.name)

    if file2.name.endswith(".csv"):
        df = pd.read_csv(file2)
        st.dataframe(df)

    elif file2.name.endswith(".xlsx"):
        df = pd.read_excel(file2)
        st.dataframe(df)

    elif file2.name.endswith((".jpg", ".png")):
        st.image(file2, caption=file2.name, width=250)
