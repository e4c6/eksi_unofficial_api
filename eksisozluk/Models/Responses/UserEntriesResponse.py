from eksisozluk.Models.Responses.ResponseMessage import Message
from eksisozluk.Models.User.EntrySummary import EntrySummary
from eksisozluk.Models.__init__ import *


@dataclass
class UserEntries:
    pinned_entry: None
    entries: List[EntrySummary]
    page_count: int
    page_size: int
    page_index: int

    @staticmethod
    def from_dict(obj: Any) -> 'UserEntries':
        assert isinstance(obj, dict)
        pinned_entry = from_none(obj.get("PinnedEntry"))
        entries = from_list(EntrySummary.from_dict, obj.get("Entries"))
        page_count = from_int(obj.get("PageCount"))
        page_size = from_int(obj.get("PageSize"))
        page_index = from_int(obj.get("PageIndex"))
        return UserEntries(pinned_entry, entries, page_count, page_size, page_index)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PinnedEntry"] = from_none(self.pinned_entry)
        result["Entries"] = from_list(lambda x: to_class(EntrySummary, x), self.entries)
        result["PageCount"] = from_int(self.page_count)
        result["PageSize"] = from_int(self.page_size)
        result["PageIndex"] = from_int(self.page_index)
        return result


@dataclass
class UserEntriesResponse:
    success: bool
    data: UserEntries
    message: Optional[Message] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserEntriesResponse':
        assert isinstance(obj, dict)
        success = from_bool(obj.get("Success"))
        message = from_union([from_none, Message], obj.get("Message"))
        data = UserEntries.from_dict(obj.get("Data"))
        return UserEntriesResponse(success, message, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Success"] = from_bool(self.success)
        result["Message"] = from_union([from_none, lambda x: to_enum(Message, x)], self.message)
        result["Data"] = to_class(UserEntries, self.data)
        return result


def user_entries_response_from_dict(s: Any) -> UserEntriesResponse:
    return UserEntriesResponse.from_dict(s)


def user_entries_response_to_dict(x: UserEntriesResponse) -> Any:
    return to_class(UserEntriesResponse, x)
