import streamlit as st

st.title("Signup Form")

name = st.text_input("Full Name")
email = st.text_input("Email Address")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Sign Up"):
    if password != confirm_password:
        st.error("Passwords do not match")
    else:
        st.success("Account created successfully!")
        st.write("Name:", name)
        st.write("Email:", email)