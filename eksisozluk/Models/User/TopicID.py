from dataclasses import dataclass
from typing import Any

from eksisozluk.Models import from_int, from_str, to_class
from eksisozluk.Models.User.TopicTitle import TopicTitle


@dataclass
class TopicID:
    id: int
    topic_title: TopicTitle
    title: str

    @staticmethod
    def from_dict(obj: Any) -> 'TopicID':
        assert isinstance(obj, dict)
        id = from_int(obj.get("Id"))
        topic_title = TopicTitle.from_dict(obj.get("TopicTitle"))
        title = from_str(obj.get("Title"))
        return TopicID(id, topic_title, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_int(self.id)
        result["TopicTitle"] = to_class(TopicTitle, self.topic_title)
        result["Title"] = from_str(self.title)
        return result