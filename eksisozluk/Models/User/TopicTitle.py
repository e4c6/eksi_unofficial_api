from dataclasses import dataclass
from typing import Any

from eksisozluk.Models import from_str, from_none


@dataclass
class TopicTitle:
    title: str
    kind: None

    @staticmethod
    def from_dict(obj: Any) -> 'TopicTitle':
        assert isinstance(obj, dict)
        title = from_str(obj.get("Title"))
        kind = from_none(obj.get("Kind"))
        return TopicTitle(title, kind)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Title"] = from_str(self.title)
        result["Kind"] = from_none(self.kind)
        return result