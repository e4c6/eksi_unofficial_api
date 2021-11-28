from dataclasses import dataclass
from typing import List, Any, Optional

from eksisozluk.Models import from_int, from_str, from_list, from_none, from_bool, from_union, to_class
from eksisozluk.Models.Entry.Entry import Entry
from eksisozluk.Models.User.EntryCounts import EntryCounts
from eksisozluk.Models.Topic.Video import Video


@dataclass
class Topic:
    id: int
    title: str
    entries: List[Entry]
    page_count: int
    page_size: int
    page_index: int
    pinned_entry: None
    entry_counts: EntryCounts
    draft_entry: None
    is_tracked: bool
    is_trackable: bool
    disambiguations: List[Any]
    is_ama_topic: bool
    matter_count: int
    slug: Optional[str] = None
    video: Optional[Video] = None

    def get_first_entry(self) -> Optional[Entry]:
        if len(self.entries) > 0:
            return self.entries[0]
        return None

    @staticmethod
    def from_dict(obj: Any) -> 'Topic':
        assert isinstance(obj, dict)
        id = from_int(obj.get("Id"))
        title = from_str(obj.get("Title"))
        entries = from_list(Entry.from_dict, obj.get("Entries"))
        page_count = from_int(obj.get("PageCount"))
        page_size = from_int(obj.get("PageSize"))
        page_index = from_int(obj.get("PageIndex"))
        pinned_entry = from_none(obj.get("PinnedEntry"))
        entry_counts = EntryCounts.from_dict(obj.get("EntryCounts"))
        draft_entry = from_none(obj.get("DraftEntry"))
        is_tracked = from_bool(obj.get("IsTracked"))
        is_trackable = from_bool(obj.get("IsTrackable"))
        disambiguations = from_list(lambda x: x, obj.get("Disambiguations"))
        is_ama_topic = from_bool(obj.get("IsAmaTopic"))
        matter_count = from_int(obj.get("MatterCount"))
        slug = from_union([from_none, from_str], obj.get("Slug"))
        video = from_union([Video.from_dict, from_none], obj.get("Video"))
        return Topic(id, title, entries, page_count, page_size, page_index, pinned_entry, entry_counts, draft_entry, is_tracked, is_trackable, disambiguations, is_ama_topic, matter_count, slug, video)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_int(self.id)
        result["Title"] = from_str(self.title)
        result["Entries"] = from_list(lambda x: to_class(Entry, x), self.entries)
        result["PageCount"] = from_int(self.page_count)
        result["PageSize"] = from_int(self.page_size)
        result["PageIndex"] = from_int(self.page_index)
        result["PinnedEntry"] = from_none(self.pinned_entry)
        result["EntryCounts"] = to_class(EntryCounts, self.entry_counts)
        result["DraftEntry"] = from_none(self.draft_entry)
        result["IsTracked"] = from_bool(self.is_tracked)
        result["IsTrackable"] = from_bool(self.is_trackable)
        result["Disambiguations"] = from_list(lambda x: x, self.disambiguations)
        result["IsAmaTopic"] = from_bool(self.is_ama_topic)
        result["MatterCount"] = from_int(self.matter_count)
        result["Slug"] = from_union([from_none, from_str], self.slug)
        result["Video"] = from_union([lambda x: to_class(Video, x), from_none], self.video)
        return result