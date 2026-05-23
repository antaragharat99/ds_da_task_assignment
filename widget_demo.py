import streamlit as st

st.title("Streamlit Widgets Demo")

if st.button("Click Me"):
   st.write("Button Pressed!")

name = st.text_input("Enter your name:")

age = st.number_input("Enter your age:", min_value = 1, max_value = 100, step = 1)

marks = st.slider("Select your marks:", 0, 100, 50)

agree = st.checkbox("I agree to terms")

gender = st.radio("Select gender:", ["Male", "Female", "Other"])

course = st.selectbox("Select your course:", ["Python", "Data Science", "Data Anlysts", "AI", "ML"])

hobbies = st.multiselect("Select your hobbies", ["Reading", "Coding", "Music", "Sports"])

if st.button("Show Results"):
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Marks:", marks)
    st.write("Agreement:", agree)
    st.write("Gender:", gender)
    st.write("Course:", course)
    st.write("Hobbies:", hobbies)