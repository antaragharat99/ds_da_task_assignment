import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st

data = pd.read_csv("students_scores.csv")

X = data[["hours_studied", "previous_score"]]
y = data["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(len(X_train), len(X_test))
st.write(X_train)