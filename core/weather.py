import requests

# =========================
# 城市映射（中文支持）
# =========================
CITY_MAP = {
    "北京": "Beijing",
    "上海": "Shanghai",
    "广州": "Guangzhou",
    "深圳": "Shenzhen",
    "郑州": "Zhengzhou",
    "河南": "Zhengzhou"
}


# =========================
# 1️⃣ 腾讯天气（主源）
# =========================
def get_weather_tencent(city: str):
    url = "https://wis.qq.com/weather/common"

    params = {
        "source": "pc",
        "weather_type": "observe",
        "city": city
    }

    res = requests.get(url, params=params, timeout=5)
    data = res.json()

    observe = data["data"]["observe"]

    return {
        "temp": float(observe["degree"]),
        "weather": observe["weather"],
        "humidity": observe["humidity"],
        "wind": observe["wind_power"],
        "source": "Tencent"
    }


# =========================
# 2️⃣ Open-Meteo（备用源）
# =========================
def get_weather_openmeteo(city: str):
    """
    用固定城市坐标（示例：北京）
    可扩展 geocoding
    """

    geo_map = {
        "Beijing": (39.9042, 116.4074),
        "Shanghai": (31.2304, 121.4737),
        "Guangzhou": (23.1291, 113.2644),
        "Shenzhen": (22.5431, 114.0579),
        "Zhengzhou": (34.7466, 113.6254)
    }

    if city not in geo_map:
        city = "Beijing"

    lat, lon = geo_map[city]

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    res = requests.get(url, params=params, timeout=5)
    data = res.json()

    w = data["current_weather"]

    return {
        "temp": w["temperature"],
        "weather": "OpenMeteo Weather",
        "humidity": 50,
        "wind": w["windspeed"],
        "source": "Open-Meteo"
    }


# =========================
# 3️⃣ 双源统一接口（核心）
# =========================
def get_weather(city: str):
    city_en = CITY_MAP.get(city, city)

    # ① 腾讯优先
    try:
        return get_weather_tencent(city_en)
    except Exception:
        pass

    # ② Open-Meteo备用
    try:
        return get_weather_openmeteo(city_en)
    except Exception:
        pass

    # ③ 完全兜底
    return None


# =========================
# 4️⃣ 运动建议
# =========================
def weather_advice(temp: float, weather: str):

    tips = []

    if temp >= 35:
        tips.append("🔥 极端高温，不建议户外运动")
    elif temp >= 30:
        tips.append("🥵 高温天气，建议降低配速")
    elif temp >= 15:
        tips.append("🏃 适合乐跑")
    elif temp >= 5:
        tips.append("🌤 可慢跑")
    else:
        tips.append("❄️ 寒冷天气注意保暖")

    if "雨" in weather:
        tips.append("🌧 雨天建议室内运动")

    return "；".join(tips)