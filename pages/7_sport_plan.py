import streamlit as st
from core.sports import sport_advice

st.title("🏃 运动建议")

level = st.selectbox("活动等级", ["久坐", "轻度", "中度", "高度活跃", "非常活跃"])

st.write(sport_advice(level))