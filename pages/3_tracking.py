import streamlit as st
from datetime import datetime

from data.tracker_db import (
    get_last_n,
    add_record,
    get_all_records
)

from core.trend import weight_trend
from core.pattern import (
    detect_overeating,
    detect_low_activity,
    detect_sleep_deprivation
)
from core.feedback import generate_feedback

st.set_page_config(page_title="智能健康追踪系统", layout="wide")

st.title("📊 智能健康追踪系统")

# =========================
# 📌 1. 添加数据模块（闭环入口）
# =========================
st.subheader("➕ 今日健康数据录入")

with st.form("add_record_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        weight = st.number_input("体重(kg)", min_value=1.0, value=60.0)

    with col2:
        calorie_intake = st.number_input("摄入热量(kcal)", min_value=0, value=2000)

    with col3:
        calorie_burn = st.number_input("消耗热量(kcal)", min_value=0, value=500)

    col4, col5 = st.columns(2)

    with col4:
        steps = st.number_input("步数", min_value=0, value=7000)

    with col5:
        sleep_hours = st.number_input("睡眠时间(h)", min_value=0.0, max_value=12.0, value=7.0)

    submitted = st.form_submit_button("💾 保存记录")

    if submitted:
        add_record({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "weight": weight,
            "calorie_intake": calorie_intake,
            "calorie_burn": calorie_burn,
            "steps": steps,
            "sleep_hours": sleep_hours
        })

        st.success("✅ 数据已保存")
        st.rerun()

st.divider()

# =========================
# 📌 2. 获取数据（防空处理）
# =========================
records = get_last_n(7)

if not records:
    st.warning("⚠️ 暂无数据，请先录入今日健康记录")
    st.stop()

# =========================
# 📌 3. 数据拆解
# =========================
weights = [r["weight"] for r in records]
intake = [r["calorie_intake"] for r in records]
steps = [r["steps"] for r in records]
sleep = [r["sleep_hours"] for r in records]

# =========================
# 📌 4. 核心分析
# =========================
trend = weight_trend(weights)

overeating = detect_overeating(intake)
low_activity = detect_low_activity(steps)
bad_sleep = detect_sleep_deprivation(sleep)

feedback = generate_feedback(
    trend,
    overeating,
    low_activity,
    bad_sleep
)

# =========================
# 📌 5. KPI 仪表盘
# =========================
st.subheader("📈 健康数据概览")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📉 体重趋势", trend)

with col2:
    st.metric("🍱 平均摄入", f"{sum(intake)/len(intake):.0f} kcal")

with col3:
    st.metric("🏃 平均步数", f"{sum(steps)/len(steps):.0f}")

with col4:
    st.metric("😴 平均睡眠", f"{sum(sleep)/len(sleep):.1f} h")

st.divider()

# =========================
# 📌 6. 风险分析
# =========================
st.subheader("⚠️ 健康风险评估")

risk = []

if overeating:
    risk.append("🍔 存在暴食倾向")

if low_activity:
    risk.append("🏃 活动量不足")

if bad_sleep:
    risk.append("😴 睡眠质量偏低")

if not risk:
    st.success("✅ 当前状态良好，继续保持")
else:
    for r in risk:
        st.warning(r)

st.divider()

# =========================
# 📌 7. AI健康建议
# =========================
st.subheader("🧠 智能健康建议")

for tip in feedback:
    st.write("•", tip)

st.divider()

# =========================
# 📌 8. 趋势可视化
# =========================
st.subheader("📊 7日趋势图")

chart_data = {
    "体重": weights,
    "摄入": intake,
    "步数": steps,
    "睡眠": sleep
}

st.line_chart(chart_data)

st.divider()

# =========================
# 📌 9. 历史记录展示
# =========================
st.subheader("📋 历史记录")

all_records = get_all_records()

for r in reversed(all_records[-7:]):
    with st.expander(f"📅 {r['date']}"):
        st.write(f"体重：{r['weight']} kg")
        st.write(f"摄入：{r['calorie_intake']} kcal")
        st.write(f"消耗：{r['calorie_burn']} kcal")
        st.write(f"步数：{r['steps']}")
        st.write(f"睡眠：{r['sleep_hours']} h")