import streamlit as st
import pandas as pd

st.title("Brazil E-Commerce Sales Analysis")

df = pd.read_csv("data/your_dataset.csv")  # adjust path

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Payment Type Distribution")
st.bar_chart(df["payment_type"].value_counts())
