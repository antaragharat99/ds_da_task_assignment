import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("salary.csv")

model = LinearRegression()
model.fit(df[["Experience"]], df["Salary"])

df["Predicted"] = model.predict(df["Salary"])   # for display only

st.header("Salary Prediction App")
st.line_chart(df.set_index("Experience")[["Salary"]])
st.line_chart(df.set_index("Experience")[["Salary"]])