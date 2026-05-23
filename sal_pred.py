import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("student_record.csv")

# Input and Output
X = df[["Hours"]]
y = df["Pass"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3
)

# Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, pred)

# Output
st.subheader("Model Accuracy")

st.metric(
    "Accuracy",
    f"{acc * 100:.2f}%"
)