import streamlit as st

st.set_page_config(
    page_title="蓬勃悦瘦",
    layout="wide"
)

st.title("🏃‍♂️ 蓬勃悦瘦")

st.markdown("""
蓬勃悦瘦：

- 🔥 热量计算
- 🍱 饮食记录
- 📊 热量跟踪
- 🧠 健康评估
- 🌦 天气与运动建议

请在左侧选择功能模块 👈
""")

# 分割线
st.divider()

# 底部信息区
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🙏 致谢")
    st.markdown("""
    本项目开发过程中，借鉴了两个优秀的开源项目，在此致以诚挚感谢：

    - **Health_Guardian**（作者：SRInternet）：[GitHub仓库](https://github.com/SRInternet/Health_Guardian)
      多学科融合架构、模块化设计思路及健康数据分析逻辑为项目提供了核心参考
    - **calories**（作者：likemayo）：[GitHub仓库](https://github.com/likemayo/calories)
      卡路里计算模型、饮食记录模块及移动端适配方案提供了重要借鉴

    感谢所有开源社区建设者的无私贡献。
    """)

with col2:
    st.subheader("⚠️ 免责声明")
    st.warning("""
    1. 本项目仅用于**个人学习与非商业用途**，所有参考代码均遵循原项目MIT开源协议规范。
    2. 本项目提供的所有健康数据计算、饮食建议及运动指导**仅为参考信息**，不构成医疗诊断、治疗或专业健康管理建议。
    3. 因使用本项目产生的任何直接或间接后果（包括但不限于健康决策失误、数据异常），项目开发者不承担任何法律责任。
    4. 本项目按"现状"提供，不附带任何明示或暗示的担保。
    5. 禁止将本项目用于非法、侵权或违反公序良俗的用途。
    """)

# 版权信息
st.caption("© 2026 蓬勃悦瘦 | MIT License")