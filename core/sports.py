def sport_advice(level):
    advice = {
        "久坐": "建议每周至少跑步2次",
        "轻度": "保持节奏，可增加强度",
        "中度": "状态良好，注意恢复",
        "高度活跃": "注意拉伸和防伤",
        "非常活跃": "注意过度训练风险"
    }
    return advice.get(level, "")