import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(
    page_title="Blinkit Dashboard",
    layout="wide"
)

# --------------------------------
# LOAD DATA
# --------------------------------
df = pd.read_csv("BlinkIT_Grocery_Data.csv")

df.columns = df.columns.str.strip()

# --------------------------------
# SIDEBAR
# --------------------------------
st.sidebar.title("🟡 Blinkit Dashboard")

item_type = st.sidebar.selectbox(
    "Item Type",
    ["All"] + list(df["Item Type"].unique())
)

outlet_size = st.sidebar.selectbox(
    "Outlet Size",
    ["All"] + list(df["Outlet Size"].dropna().unique())
)

location = st.sidebar.selectbox(
    "Outlet Location",
    ["All"] + list(df["Outlet Location Type"].unique())
)

# --------------------------------
# FILTER DATA
# --------------------------------
filtered_df = df.copy()

if item_type != "All":
    filtered_df = filtered_df[
        filtered_df["Item Type"] == item_type
    ]

if outlet_size != "All":
    filtered_df = filtered_df[
        filtered_df["Outlet Size"] == outlet_size
    ]

if location != "All":
    filtered_df = filtered_df[
        filtered_df["Outlet Location Type"] == location
    ]

# --------------------------------
# KPI
# --------------------------------
sales = filtered_df["Sales"].sum()
avg_sales = filtered_df["Sales"].mean()
items = filtered_df.shape[0]
rating = filtered_df["Rating"].mean()

st.title("📊 Blinkit Sales Dashboard")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Sales", f"₹ {sales:,.0f}")
c2.metric("Avg Sales", f"₹ {avg_sales:,.0f}")
c3.metric("No of Items", items)
c4.metric("Rating", f"{rating:.1f}")

# --------------------------------
# ROW 1
# --------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Item Fat Content")

    fat = filtered_df.groupby(
        "Item Fat Content"
    )["Sales"].sum()

    fig1, ax1 = plt.subplots()
    ax1.pie(
        fat,
        labels=fat.index,
        autopct="%1.1f%%"
    )
    st.pyplot(fig1)

with col2:
    st.subheader("Sales by Item Type")

    item = filtered_df.groupby(
        "Item Type"
    )["Sales"].sum().sort_values().tail(10)

    fig2, ax2 = plt.subplots(figsize=(8,5))
    ax2.barh(item.index, item.values)
    st.pyplot(fig2)

# --------------------------------
# ROW 2
# --------------------------------
col3, col4 = st.columns(2)

with col3:
    st.subheader("Outlet Location")

    loc = filtered_df.groupby(
        "Outlet Location Type"
    )["Sales"].sum()

    fig3, ax3 = plt.subplots()
    ax3.bar(loc.index, loc.values)
    st.pyplot(fig3)

with col4:
    st.subheader("Outlet Size")

    size = filtered_df.groupby(
        "Outlet Size"
    )["Sales"].sum()

    fig4, ax4 = plt.subplots()
    ax4.pie(
        size,
        labels=size.index,
        autopct="%1.1f%%"
    )
    st.pyplot(fig4)

# --------------------------------
# TABLE
# --------------------------------
st.subheader("Outlet Summary")

summary = filtered_df.groupby(
    "Outlet Type"
).agg({
    "Sales": "sum",
    "Rating": "mean",
    "Item Identifier": "count"
}).reset_index()

summary.columns = [
    "Outlet Type",
    "Total Sales",
    "Avg Rating",
    "No of Items"
]

st.dataframe(summary, use_container_width=True)