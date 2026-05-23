import streamlit as st

st.sidebar.title("Addition of Two Numbers")

num1 = st.sidebar.number_input("Enter first number", value=0)
num2 = st.sidebar.number_input("Enter second number", value=0)

st.header("Result will display here")
if st.sidebar.button("Add"):
    result = num1 + num2
    st.success(f"Result: {result}")