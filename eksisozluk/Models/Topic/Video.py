from dataclasses import dataclass
from typing import Any

from eksisozluk.Models import from_none, from_bool


@dataclass
class Video:
    display_info: None
    in_topic_video: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Video':
        assert isinstance(obj, dict)
        display_info = from_none(obj.get("DisplayInfo"))
        in_topic_video = from_bool(obj.get("InTopicVideo"))
        return Video(display_info, in_topic_video)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DisplayInfo"] = from_none(self.display_info)
        result["InTopicVideo"] = from_bool(self.in_topic_video)
        return result