def generate_feedback(trend, overeating, low_activity, bad_sleep):
    advice = []

    if trend == "increasing":
        advice.append("⚠️ 体重上升，请控制热量摄入")

    if overeating:
        advice.append("🍔 检测到暴食，建议减少高热量食物")

    if low_activity:
        advice.append("🏃 活动量偏低，每天至少6000步")

    if bad_sleep:
        advice.append("😴 睡眠不足会影响减脂")

    if not advice:
        advice.append("✅ 状态良好，继续保持")

    return advice