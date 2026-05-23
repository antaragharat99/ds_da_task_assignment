import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "Experience": [ 1, 2, 3, 4, 5, 6],
    "Salary": [20000, 25000, 30000, 35000, 40000, 45000]
})

df = pd.DataFrame(data)

X = df[['Experience']]
Y = df['Salary']

model = LinearRegression()
model.fit(X, Y)

st.title("Employee salary prediction")

exp = st.number_input("Enter your experience (in years):", min_value = 0, max_value = 40, step = 1)

if st.button("Predict Salary"):
   salary = model.predict([[exp]])
   st.write("Predict Salary:", int(salary[0]))