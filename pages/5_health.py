import streamlit as st
from core.health import calculate_bmi, sleep_score

st.title("🧠 健康评估")

w = st.number_input("体重 (kg)", min_value=1.0, value=60.0)
h = st.number_input("身高 (cm)", min_value=1.0, value=170.0)

if st.button("计算 BMI"):
    bmi, status = calculate_bmi(w, h)

    if bmi is None:
        st.error(status)
    else:
        st.metric("BMI", bmi)
        st.write("健康状态：", status)

bmi, status = calculate_bmi(w, h)

st.write(bmi, status)

sleep = st.slider("睡眠时长", 0, 12)
wake = st.slider("夜醒次数", 0, 5)
reg = st.checkbox("作息规律")

score = sleep_score(sleep, wake, reg)

st.write("睡眠评分:", score)