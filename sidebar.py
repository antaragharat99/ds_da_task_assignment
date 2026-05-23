import streamlit as st

st.title("Product Store")

# --- Sidebar Section ---
st.sidebar.header("Filters")

# Filter dropdown
category = st.sidebar.selectbox(
    "Select Category",
    ["Fruits", "Vegetables", "Snacks"]
)

# Price range slider
price_range = st.sidebar.slider(
    "Select Price Range",
    0, 1000, (50, 250)   
)

# Delivery location input
location = st.sidebar.text_input("Enter Delivery Location")

# --- Main Screen ---
st.write("### Selected Filters")

st.write("**Category:**", category)
st.write("**Price Range:**", price_range)
st.write("**Delivery Location:**", location)