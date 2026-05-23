import streamlit as st
import pandas as pd

st.title("Flipkart Simple Dashboard")

df = pd.read_csv("flipkart_data.csv")

st.subheader("Full Dataset")
st.dataframe(df)

st.title("Flipkart KPI Dashboard")

total_orders = df["Orders"].sum()
avg_price = int(df["Price"].mean())
avg_rating = round(df["Rating"].mean(), 2)

st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Orders", total_orders)
col2.metric("Average Price", avg_price)
col3.metric("Average Rating", avg_rating)

st.title("Flipkart Filter Dashboard")

category = st.selectbox("Select Category", ["All"] + sorted(df["Category"].unique().tolist()))
city = st.selectbox("Select City", ["All"] + sorted(df["City"].unique().tolist()))

filtered_df = df

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

if city != "All":
    filtered_df = filtered_df[filtered_df["City"] == city]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

st.title("Flipkart Sales Chart")

category = st.selectbox("Category", sorted(df["Category"].unique().tolist()))

filtered_df = df[df["Category"] == category]

st.subheader("Orders by Product")
chart_df = filtered_df.set_index("Product")[["Orders"]]
st.bar_chart(chart_df)