from dataclasses import dataclass
from typing import Any

from eksisozluk.Models import from_int


@dataclass
class PinnedEntryEntryCounts:
    before_first_entry: int
    after_last_entry: int
    buddy: int
    total: int

    @staticmethod
    def from_dict(obj: Any) -> 'PinnedEntryEntryCounts':
        assert isinstance(obj, dict)
        before_first_entry = from_int(obj.get("BeforeFirstEntry"))
        after_last_entry = from_int(obj.get("AfterLastEntry"))
        buddy = from_int(obj.get("Buddy"))
        total = from_int(obj.get("Total"))
        return PinnedEntryEntryCounts(before_first_entry, after_last_entry, buddy, total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["BeforeFirstEntry"] = from_int(self.before_first_entry)
        result["AfterLastEntry"] = from_int(self.after_last_entry)
        result["Buddy"] = from_int(self.buddy)
        result["Total"] = from_int(self.total)
        return result