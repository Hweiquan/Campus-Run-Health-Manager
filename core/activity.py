def get_activity_level(freq, pace):
    if freq < 1:
        return "久坐"
    elif 1 <= freq <= 3 and 6.5 <= pace <= 8.5:
        return "轻度"
    elif 3 < freq <= 5 and 5.5 <= pace < 6.5:
        return "中度"
    elif 5 < freq <= 7 and 5.0 <= pace < 5.5:
        return "高度活跃"
    elif freq == 7 and pace < 5.0:
        return "非常活跃"
    else:
        return "轻度"