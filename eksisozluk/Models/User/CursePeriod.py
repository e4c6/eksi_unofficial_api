from dataclasses import dataclass
from datetime import datetime
from typing import Any

from eksisozluk.Models import from_datetime


@dataclass
class CursePeriod:
    curse_period_from: datetime
    to: datetime

    @staticmethod
    def from_dict(obj: Any) -> 'CursePeriod':
        assert isinstance(obj, dict)
        curse_period_from = from_datetime(obj.get("From"))
        to = from_datetime(obj.get("To"))
        return CursePeriod(curse_period_from, to)

    def to_dict(self) -> dict:
        result: dict = {}
        result["From"] = self.curse_period_from.isoformat()
        result["To"] = self.to.isoformat()
        return result