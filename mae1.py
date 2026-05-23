from sklearn.metrics import mean_absolute_error
import streamlit as st

actual = [50, 60, 70]
Predicted = [52, 58, 75]

mae = mean_absolute_error(actual, Predicted)
st.write(mae)