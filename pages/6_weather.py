import streamlit as st
from core.weather import get_weather, weather_advice

st.set_page_config(page_title="天气系统", layout="wide")

st.title("🌦 校园天气 & 乐跑智能系统（双源稳定版）")

# =========================
# 输入
# =========================
city = st.text_input("请输入城市（支持中文，如：北京 / 上海 / 郑州）", "北京")

# =========================
# 获取天气
# =========================
if st.button("🌤 获取天气"):

    data = get_weather(city)

    # =========================
    # ⭐ 关键兜底（你要求加的）
    # =========================
    if data is None:
        st.warning("⚠️ 天气接口暂时不可用，显示默认数据")

        data = {
            "temp": 25,
            "weather": "未知",
            "humidity": 50,
            "wind": 2,
            "source": "Default"
        }

    # =========================
    # 展示
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🌡 温度", f"{data['temp']} °C")

    with col2:
        st.metric("💧 湿度", f"{data['humidity']} %")

    with col3:
        st.metric("🌬 风力", f"{data['wind']}")

    st.success(f"当前天气：{data['weather']}")
    st.caption(f"数据来源：{data['source']}")

    st.divider()

    # =========================
    # 运动分析
    # =========================
    st.subheader("🏃 乐跑运动建议")

    advice = weather_advice(data["temp"], data["weather"])
    st.info(advice)

    # =========================
    # 风险等级
    # =========================
    temp = data["temp"]

    if temp >= 35:
        st.error("🔥 极端高温风险")
    elif temp >= 30:
        st.warning("🥵 高温风险")
    elif temp <= 5:
        st.warning("❄️ 低温风险")
    else:
        st.success("✅ 适合运动")

    # =========================
    # 调试信息
    # =========================
    with st.expander("📊 原始数据"):
        st.json(data)