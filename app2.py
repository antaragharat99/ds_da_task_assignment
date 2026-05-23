import streamlit as st
import pandas as pd

data = pd.DataFrame({"marks": [50,60,70,80,90]})
st.line_chart(data)