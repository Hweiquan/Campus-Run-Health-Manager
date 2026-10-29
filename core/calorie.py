from config.settings import ACTIVITY_FACTORS, CALORIE_DEFICIT
from core.activity import get_activity_level

def calculate_bmr(weight, height, age, gender):
    if gender == "男":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_all(weight, height, age, gender, freq, pace, goal):

    bmr = calculate_bmr(weight, height, age, gender)
    level = get_activity_level(freq, pace)
    tdee = bmr * ACTIVITY_FACTORS[level]
    deficit = CALORIE_DEFICIT[goal]

    target = tdee - deficit

    return {
        "BMR": round(bmr, 1),
        "level": level,
        "TDEE": round(tdee, 1),
        "target": round(target, 1),
        "deficit": deficit
    }