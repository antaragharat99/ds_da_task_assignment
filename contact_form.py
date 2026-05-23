import streamlit as st

st.title("Contact Us")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("Message sent successfully!")
        st.write("Message Summary:")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Message:", message)
    else:
        st.error("Please fill all fields")