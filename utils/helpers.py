import streamlit as st
from datetime import datetime
import pandas as pd

# 初始化
def init_session():
    if "diet" not in st.session_state:
        st.session_state.diet = []

# 添加
def add_food(name, cal, meal):
    st.session_state.diet.append({
        "name": name,
        "cal": cal,
        "meal": meal,
        "time": datetime.now().strftime("%H:%M")
    })

# 删除
def delete_food(index):
    st.session_state.diet.pop(index)

# 编辑
def update_food(index, name, cal, meal):
    st.session_state.diet[index] = {
        "name": name,
        "cal": cal,
        "meal": meal,
        "time": datetime.now().strftime("%H:%M")
    }

# 清空
def clear_diet():
    st.session_state.diet = []

# 转 DataFrame（用于图表/导出）
def get_diet_df():
    return pd.DataFrame(st.session_state.diet)

def total_calories():
    return sum(item["cal"] for item in st.session_state.diet)