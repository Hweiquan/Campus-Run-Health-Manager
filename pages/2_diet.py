import streamlit as st
import pandas as pd
from utils.helpers import *

init_session()

st.title("🍱 智能饮食管理")

# ================= 添加模块 =================
with st.expander("➕ 添加食物", expanded=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        name = st.text_input("食物名称")

    with col2:
        cal = st.number_input("热量 (kcal)", min_value=0.0)

    with col3:
        meal = st.selectbox(
            "餐次",
            ["早餐", "午餐", "晚餐", "加餐"],
            key="meal_add"
        )

    if st.button("添加记录"):
        if name and cal > 0:
            add_food(name, cal, meal)
            st.success("添加成功")
            st.rerun()
        else:
            st.warning("请输入有效数据")

# ================= 数据展示 =================
st.subheader("📊 今日饮食")

if len(st.session_state.diet) == 0:
    st.info("暂无数据")
else:
    df = get_diet_df()

    # 🔥 总热量
    total = df["cal"].sum()
    st.metric("🔥 今日摄入", f"{total:.0f} kcal")

    # ================= 分类展示 =================
    meals = ["早餐", "午餐", "晚餐", "加餐"]

    for m in meals:
        st.markdown(f"### 🍽 {m}")
        meal_df = df[df["meal"] == m]

        if meal_df.empty:
            st.write("无")
        else:
            for i, row in meal_df.iterrows():
                col1, col2, col3, col4, col5 = st.columns([3,2,2,2,2])

                with col1:
                    st.write(row["name"])
                with col2:
                    st.write(f"{row['cal']} kcal")
                with col3:
                    st.write(row["time"])
                with col4:
                    if st.button("✏️", key=f"edit_{i}"):
                        st.session_state.edit_index = i
                with col5:
                    if st.button("❌", key=f"del_{i}"):
                        delete_food(i)
                        st.rerun()

    # ================= 编辑模块 =================
    if "edit_index" in st.session_state:
        idx = st.session_state.edit_index
        st.divider()
        st.subheader("✏️ 编辑记录")

        item = st.session_state.diet[idx]

        new_name = st.text_input("名称", value=item["name"])
        new_cal = st.number_input("热量", value=float(item["cal"]))
        new_meal = st.selectbox(
            "餐次",
            ["早餐", "午餐", "晚餐", "加餐"],
            index=["早餐","午餐","晚餐","加餐"].index(item["meal"])
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("保存修改"):
                update_food(idx, new_name, new_cal, new_meal)
                del st.session_state.edit_index
                st.success("修改成功")
                st.rerun()

        with col2:
            if st.button("取消"):
                del st.session_state.edit_index
                st.rerun()

    # ================= 图表分析 =================
    st.divider()
    st.subheader("📈 饮食结构")

    chart_df = df.groupby("meal")["cal"].sum()

    st.bar_chart(chart_df)

    # ================= 操作区 =================
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🗑 清空所有记录"):
            clear_diet()
            st.rerun()

    with col2:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 导出 CSV",
            csv,
            "diet_data.csv",
            "text/csv"
        )