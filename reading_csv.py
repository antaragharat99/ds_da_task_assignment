import streamlit as st
import pandas as pd

df = pd.read_csv("student.csv")
st.dataframe(df)

st.header("Student Marks Table")
st.dataframe(df)

st.subheader("Average Marks")
st.write(df[["Maths", "Science", "English"]].mean())

file = st.file_uploader("Upload CSV file")

if file:
    df = pd.read_csv(file)
    st.dataframe(df)

st.line_chart(df[["Maths", "Science", "English"]])