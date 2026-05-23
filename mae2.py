import streamlit as st
import pandas as pd

from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression

df = pd.read_csv("salary.csv")

model = LinearRegression()
model.fit(df[["Experience"]], df["Salary"])

pred = model.predict(df[["Experience"]])

mae = mean_absolute_error(df["Salary"], pred)

st.subheader("Mean Absolute Error")

st.write("Average Error:", round(mae, 2))