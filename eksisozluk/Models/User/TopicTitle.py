from eksisozluk.Models.__init__ import *
from eksisozluk.Models import from_str, from_none


@dataclass
class TopicTitle:
    title: Optional[str] = None
    kind: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TopicTitle':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("Title"))
        kind = from_union([from_str, from_none], obj.get("Kind"))
        return TopicTitle(title, kind)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Title"] = from_union([from_str, from_none], self.title)
        result["Kind"] = from_union([from_str, from_none], self.kind)
        return result