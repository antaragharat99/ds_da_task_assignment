import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Simple Salary Prediction App")

df = pd.read_csv("salary1.csv")

st.subheader("Salary Dataset")
st.dataframe(df)

model = LinearRegression()
model.fit(df[["Experience"]], df["Salary"])

exp = st.number_input("Enter Experience (in years):", 1, 50)

pred = model.predict([[exp]])

st.subheader("Predicted Salary")
st.write(int(pred[0]))