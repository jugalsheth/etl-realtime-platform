import streamlit as st
import pandas as pd
import time
import os

st.set_page_config(page_title="Real-Time Orders Dashboard", layout="wide")

FILE_PATH = "data/orders_log.csv"
refresh_interval = 2  # seconds

st.title("📊 Real-Time Orders Dashboard")

if not os.path.exists(FILE_PATH):
    st.warning("⏳ Waiting for data to stream into `orders_log.csv`...")
else:
    placeholder = st.empty()

    while True:
        df = pd.read_csv(FILE_PATH)

        if df.empty:
            st.warning("No data yet!")
            time.sleep(refresh_interval)
            continue

        df["timestamp"] = pd.to_datetime(df["timestamp"])

        with placeholder.container():
            # ==== KPIs ====
            total_orders = len(df)
            total_qty = df["qty"].sum()
            unique_items = df["item_id"].nunique()

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Orders", total_orders)
            col2.metric("Total Quantity Ordered", total_qty)
            col3.metric("Unique Items", unique_items)

            st.markdown("---")

            # ==== Bar Chart: Top Items ====
            st.subheader("📦 Top 5 Most Ordered Items")
            top_items = df.groupby("item_id")["qty"].sum().sort_values(ascending=False).head(5)
            st.bar_chart(top_items)

            # ==== Line Chart: Orders Over Time ====
            st.subheader("📈 Orders Over Time")
            df_by_time = df.set_index("timestamp").resample("5s").size()
            st.line_chart(df_by_time)

            # ==== Latest Orders Table ====
            st.subheader("📋 Latest Orders")
            st.dataframe(df.tail(20), use_container_width=True)

        time.sleep(refresh_interval)
