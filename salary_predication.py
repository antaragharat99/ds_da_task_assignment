import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Salary Prediction App")

df = pd.read_csv("salary.csv")

model = LinearRegression()
model.fit(df[["Experience"]], df["Salary"])

st.subheader("Enter Experience")

exp = st.number_input("Experience (years)", 1, 50)

pred = model.predict([[exp]])

st.subheader("Predicted Salary")

st.write(int(pred[0]))

st.line_chart(df.set_index("Experience"))


df["Predicted"] = df["Salary"]   # for display only

st.line_chart(df.set_index("Experience")[["Salary"]])
st.line_chart(df.set_index("Experience")[["Salary"]])