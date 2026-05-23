from sklearn.metrics import confusion_matrix
import streamlit as st

actual = [1, 0, 1, 1, 0]
Predicted = [1, 0, 0, 1, 0]

cm = confusion_matrix(actual, Predicted)
st.write(cm)