import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Salary Prediction with Chart")

df = pd.read_csv("salary1.csv")

model = LinearRegression()
model.fit(df[["Experience"]], df["Salary"])

st.line_chart(df.set_index("Experience"))

exp = st.slider("Experience (Years)", 1, 15)
pred = model.predict([[exp]])

st.write("Predicted Salary:", int(pred[0]))