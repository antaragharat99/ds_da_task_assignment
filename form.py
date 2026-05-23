import streamlit as st

with st.form("student_form"):
    name = st.text_input("Enter Name")
    cls = st.number_input("Enter Class", 1, 12)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("Name:", name)
    st.write("Class:", cls)


with st.form("salary_form"):

    st.subheader("Salary Prediction Form")

    exp = st.number_input("Experience (Years)", min_value=0, max_value=40, step=1, key="experience" )

    age = st.number_input("Age", min_value=18, max_value=60, step=1, key="age" )

    submit = st.form_submit_button("Predict Salary")

if submit:
    st.success("Inputs Received Successfully")
    st.write("Experience:", exp, "Years")
    st.write("Age:", age)
    st.write("Run ML Model Here")


with st.form("feedback"):
    rating = st.slider("Rate our app", 1, 5)
    comment = st.text_area("Your Feedback")
    send = st.form_submit_button("Send")

if send:
    st.write("Thanks for your feedback!")


with st.form("course_form"):
    course = st.selectbox("Choose course", ["Python", "AI", "Data Science"])
    hours = st.slider("Hours Studied", 1, 10)
    note = st.text_input("Any Note?")
    submit = st.form_submit_button("Submit")

if submit:
    st.write(course, hours, note)