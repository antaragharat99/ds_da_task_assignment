import streamlit as st

marks = st.slider("Select Marks", 0, 100, 50)
st.write("Your Marks:", marks)

course = st.selectbox("Choose Course", ["Python", "AI", "Data Science"])
st.write("Selected:", course)


show = st.checkbox("Show Message")

if show:
    st.write("Hello Student!")

age = st.slider("Age", 1, 60)
course = st.selectbox("Course", ["Python", "AI", "ML"])
mode = st.radio("Mode", ["Online", "Offline"])
agree = st.checkbox("I Agree")

if agree:
    st.write(f"Age: {age}, Course: {course}, Mode: {mode}")