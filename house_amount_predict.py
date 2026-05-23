import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "BHK": [ 1, 2],
    "Amount": [20000000, 26000000]
})

df = pd.DataFrame(data)

X = df[['BHK']]
Y = df['Amount']

model = LinearRegression()
model.fit(X, Y)

st.title("House Price Estimation")

exp = st.number_input("Enter no of BHK:", min_value = 0, max_value = 7, step = 1)

if st.button("Predict Price"):
   amount = model.predict([[exp]])
   st.success(f"Estimated House Amount: {int(amount[0])}")