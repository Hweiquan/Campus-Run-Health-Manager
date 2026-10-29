import streamlit as st
from core.calorie import calculate_all

st.title("🔥 热量计算")

w = st.number_input("体重 kg", 40, 120)
h = st.number_input("身高 cm", 140, 200)
age = st.number_input("年龄", 10, 40)
gender = st.selectbox("性别", ["男", "女"])

freq = st.slider("每周跑步次数", 0, 7)
pace = st.number_input("配速 min/km", 4.0, 10.0, 6.5)

goal = st.selectbox("目标", ["慢速", "中速", "快速"])

if st.button("计算"):
    res = calculate_all(w, h, age, gender, freq, pace, goal)
    st.write(res)