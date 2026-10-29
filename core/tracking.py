from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Dict
import json
import os

DATA_PATH = "data/tracking.json"


@dataclass
class DailyRecord:
    date: str
    weight: float
    calorie_intake: int
    calorie_burn: int
    steps: int
    sleep_hours: float


class Tracker:
    def __init__(self):
        self.records: List[DailyRecord] = []
        self.load()

    # =========================
    # 数据存取
    # =========================
    def load(self):
        if os.path.exists(DATA_PATH):
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.records = [DailyRecord(**d) for d in data]

    def save(self):
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump([asdict(r) for r in self.records], f, indent=2)

    # =========================
    # 新增记录
    # =========================
    def add_record(self, record: DailyRecord):
        self.records.append(record)
        self.save()

    # =========================
    # 获取最近N天
    # =========================
    def get_last_n_days(self, n=7):
        return sorted(self.records, key=lambda x: x.date)[-n:]

    # =========================
    # 数据提取
    # =========================
    def get_series(self, field: str):
        return [getattr(r, field) for r in self.records]

