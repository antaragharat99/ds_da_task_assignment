import streamlit as st
import pandas as pd

df = pd.read_csv("students.csv")

search = st.text_input("Search Name:")

if search:
    df = df[df["Name"].str.contains(search, case=False)]

st.dataframe(df)


classes = df["Class"].unique()

selected_class = st.selectbox("Select Class", classes)

filtered_df = df[df["Class"] == selected_class]

st.dataframe(filtered_df)


marks_range = st.slider("Select Minimum Maths Marks", 0, 100, 50)

filtered_df = df[df["Maths"] >= marks_range]

st.dataframe(filtered_df)


name = st.text_input("Search Student Name:",key="final_name")

class_selected = st.selectbox("Select Final Class",df["Class"].unique(),key="final_class")

final_df = df.copy()

if name:
    final_df = final_df[
        final_df["Name"].str.contains(name, case=False)
    ]

final_df = final_df[final_df["Class"] == class_selected]

st.subheader("Final Filtered Data")
st.dataframe(final_df)