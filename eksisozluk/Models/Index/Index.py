from dataclasses import dataclass
from typing import List, Any

from eksisozluk.Models import from_list, from_int, from_bool, from_none, to_class
from eksisozluk.Models.Index.IndexedTopic import IndexedTopic


@dataclass
class Index:
    topics: List[IndexedTopic]
    page_count: int
    page_size: int
    page_index: int
    has_pinned_index_item: bool
    pinned_index_item: None

    @staticmethod
    def from_dict(obj: Any) -> 'Index':
        assert isinstance(obj, dict)
        topics = from_list(IndexedTopic.from_dict, obj.get("Topics"))
        page_count = from_int(obj.get("PageCount"))
        page_size = from_int(obj.get("PageSize"))
        page_index = from_int(obj.get("PageIndex"))
        has_pinned_index_item = from_bool(obj.get("HasPinnedIndexItem"))
        pinned_index_item = from_none(obj.get("PinnedIndexItem"))
        return Index(topics, page_count, page_size, page_index, has_pinned_index_item, pinned_index_item)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Topics"] = from_list(lambda x: to_class(IndexedTopic, x), self.topics)
        result["PageCount"] = from_int(self.page_count)
        result["PageSize"] = from_int(self.page_size)
        result["PageIndex"] = from_int(self.page_index)
        result["HasPinnedIndexItem"] = from_bool(self.has_pinned_index_item)
        result["PinnedIndexItem"] = from_none(self.pinned_index_item)
        return result