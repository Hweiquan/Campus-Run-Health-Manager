import streamlit as st
from data.food_db import FOOD_DB

st.title("🍔 食物估算")

food = st.selectbox("选择食物", list(FOOD_DB.keys()))
amount = st.number_input("份数", 1, 10)

cal = FOOD_DB[food] * amount

st.write(f"热量: {cal}")