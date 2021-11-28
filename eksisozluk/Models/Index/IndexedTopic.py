from dataclasses import dataclass
from datetime import datetime
from typing import Any

from eksisozluk.Models import from_datetime, from_int, from_str


@dataclass
class IndexedTopic:
    day: datetime
    matched_count: int
    topic_id: int
    full_count: int
    title: str

    @staticmethod
    def from_dict(obj: Any) -> 'IndexedTopic':
        assert isinstance(obj, dict)
        day = from_datetime(obj.get("Day"))
        matched_count = from_int(obj.get("MatchedCount"))
        topic_id = from_int(obj.get("TopicId"))
        full_count = from_int(obj.get("FullCount"))
        title = from_str(obj.get("Title"))
        return IndexedTopic(day, matched_count, topic_id, full_count, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Day"] = self.day.isoformat()
        result["MatchedCount"] = from_int(self.matched_count)
        result["TopicId"] = from_int(self.topic_id)
        result["FullCount"] = from_int(self.full_count)
        result["Title"] = from_str(self.title)
        return result