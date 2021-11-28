from dataclasses import dataclass
from typing import Any

from eksisozluk.Models import from_int


@dataclass
class UserInfoEntryCounts:
    total: int
    last_month: int
    last_week: int
    today: int

    @staticmethod
    def from_dict(obj: Any) -> 'UserInfoEntryCounts':
        assert isinstance(obj, dict)
        total = from_int(obj.get("Total"))
        last_month = from_int(obj.get("LastMonth"))
        last_week = from_int(obj.get("LastWeek"))
        today = from_int(obj.get("Today"))
        return UserInfoEntryCounts(total, last_month, last_week, today)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Total"] = from_int(self.total)
        result["LastMonth"] = from_int(self.last_month)
        result["LastWeek"] = from_int(self.last_week)
        result["Today"] = from_int(self.today)
        return result