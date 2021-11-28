from dataclasses import dataclass
from typing import List, Optional, Any

from eksisozluk.Models import from_list, from_bool, from_int, from_union, from_none, from_str, to_class
from eksisozluk.Models.User.Badge import Badge
from eksisozluk.Models.Topic.Topic import Topic
from eksisozluk.Models.User.UserInfo import UserInfo


@dataclass
class User:
    user_info: UserInfo
    badges: List[Badge]
    has_entry_used_on_seyler: bool
    follower_count: int
    followings_count: int
    picture: Optional[str] = None
    pinned_entry: Optional[Topic] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        user_info = UserInfo.from_dict(obj.get("UserInfo"))
        badges = from_list(Badge.from_dict, obj.get("Badges"))
        has_entry_used_on_seyler = from_bool(obj.get("HasEntryUsedOnSeyler"))
        follower_count = from_int(obj.get("FollowerCount"))
        followings_count = from_int(obj.get("FollowingsCount"))
        picture = from_union([from_none, from_str], obj.get("Picture"))
        pinned_entry = from_union([from_none, Topic.from_dict], obj.get("PinnedEntry"))
        return User(user_info, badges, has_entry_used_on_seyler, follower_count, followings_count, picture, pinned_entry)

    def to_dict(self) -> dict:
        result: dict = {}
        result["UserInfo"] = to_class(UserInfo, self.user_info)
        result["Badges"] = from_list(lambda x: to_class(Badge, x), self.badges)
        result["HasEntryUsedOnSeyler"] = from_bool(self.has_entry_used_on_seyler)
        result["FollowerCount"] = from_int(self.follower_count)
        result["FollowingsCount"] = from_int(self.followings_count)
        result["Picture"] = from_union([from_none, from_str], self.picture)
        result["PinnedEntry"] = from_union([from_none, lambda x: to_class(Topic, x)], self.pinned_entry)
        return result