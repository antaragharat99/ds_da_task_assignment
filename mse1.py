from sklearn.metrics import mean_squared_error
import streamlit as st

actual = [10, 20, 30]
Predicted = [12, 18, 33]

mse = mean_squared_error(actual, Predicted)
st.write(mse)