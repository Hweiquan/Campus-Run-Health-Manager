def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        status = "偏瘦"
    elif bmi < 24:
        status = "正常"
    elif bmi < 28:
        status = "超重"
    else:
        status = "肥胖"

    return round(bmi, 2), status

def calculate_bmi(weight, height):
    if height is None or height <= 0:
        return None, "身高无效"

    if weight is None or weight <= 0:
        return None, "体重无效"

    height_m = height / 100

    if height_m <= 0:
        return None, "身高无效"

    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        status = "偏瘦"
    elif bmi < 24:
        status = "正常"
    elif bmi < 28:
        status = "超重"
    else:
        status = "肥胖"

    return round(bmi, 2), status

def sleep_score(hours, wake_count, regular):
    score = 100

    if hours < 7:
        score -= 20

    score -= wake_count * 10

    if not regular:
        score -= 20

    return max(score, 0)