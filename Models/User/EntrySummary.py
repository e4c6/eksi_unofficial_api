from dataclasses import dataclass
from typing import Any

from Models import to_class
from Models.Entry.Entry import Entry
from Models.User.TopicID import TopicID


@dataclass
class EntrySummary:
    topic_id: TopicID
    entry: Entry

    @staticmethod
    def from_dict(obj: Any) -> 'EntrySummary':
        assert isinstance(obj, dict)
        topic_id = TopicID.from_dict(obj.get("TopicId"))
        entry = Entry.from_dict(obj.get("Entry"))
        return EntrySummary(topic_id, entry)

    def to_dict(self) -> dict:
        result: dict = {}
        result["TopicId"] = to_class(TopicID, self.topic_id)
        result["Entry"] = to_class(Entry, self.entry)
        return result