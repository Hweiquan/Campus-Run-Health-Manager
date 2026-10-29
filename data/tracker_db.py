import json
import os
from typing import List, Dict, Any

# =========================
# 数据文件路径
# =========================
DATA_PATH = "data/tracking.json"


# =========================
# 初始化文件
# =========================
def init_db():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump([], f)


# =========================
# 读取全部数据
# =========================
def load_records() -> List[Dict[str, Any]]:
    init_db()
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================
# 写入全部数据
# =========================
def save_records(records: List[Dict[str, Any]]):
    init_db()
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


# =========================
# 增
# =========================
def add_record(record: Dict[str, Any]):
    records = load_records()
    records.append(record)
    save_records(records)


# =========================
# 删
# =========================
def delete_record(index: int):
    records = load_records()
    if 0 <= index < len(records):
        records.pop(index)
        save_records(records)


# =========================
# 改
# =========================
def update_record(index: int, new_record: Dict[str, Any]):
    records = load_records()
    if 0 <= index < len(records):
        records[index] = new_record
        save_records(records)


# =========================
# 查（全部）
# =========================
def get_all_records() -> List[Dict[str, Any]]:
    return load_records()


# =========================
# 查（最近N条）
# =========================
def get_last_n(n: int = 7) -> List[Dict[str, Any]]:
    records = load_records()
    return records[-n:]