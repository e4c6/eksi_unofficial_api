from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Any

from eksisozluk.Models import (
    from_int,
    from_str,
    from_datetime,
    from_bool,
    from_none,
    from_union,
    from_list,
    to_class,
)
from eksisozluk.Models.User.UserIdentifier import UserIdentifier


@dataclass
class CommentSummary:
    entry_id: int
    comment_id: int
    author: UserIdentifier
    created: datetime
    last_updated: Optional[datetime]
    content: str
    up_vote_count: int
    down_vote_count: int

    @staticmethod
    def from_dict(obj: Any) -> "CommentSummary":
        assert isinstance(obj, dict)
        entry_id = from_int(obj.get("EntryId"))
        comment_id = from_int(obj.get("CommentId"))
        author = UserIdentifier.from_dict(obj.get("Author"))
        created = from_datetime(obj.get("Created"))
        last_updated = from_union([from_datetime, from_none], obj.get("LastUpdated"))
        content = from_str(obj.get("Content"))
        up_vote_count = from_int(obj.get("UpVoteCount"))
        down_vote_count = from_int(obj.get("DownVoteCount"))
        return CommentSummary(
            entry_id,
            comment_id,
            author,
            created,
            last_updated,
            content,
            up_vote_count,
            down_vote_count,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["EntryId"] = from_int(self.entry_id)
        result["CommentId"] = from_int(self.comment_id)
        result["Author"] = to_class(UserIdentifier, self.author)
        result["Created"] = self.created.isoformat()
        result["LastUpdated"] = from_union(
            [lambda x: x.isoformat(), from_none], self.last_updated
        )
        result["Content"] = from_str(self.content)
        result["UpVoteCount"] = from_int(self.up_vote_count)
        result["DownVoteCount"] = from_int(self.down_vote_count)
        return result


@dataclass
class Entry:
    id: int
    content: str
    author: UserIdentifier
    created: datetime
    is_favorite: bool
    favorite_count: int
    hidden: bool
    active: bool
    comment_count: int
    comment_summary: Optional[CommentSummary]
    last_updated: Optional[datetime] = None
    avatar_url: Optional[str] = None
    media: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> "Entry":
        assert isinstance(obj, dict)
        id = from_int(obj.get("Id"))
        content = from_str(obj.get("Content"))
        author = UserIdentifier.from_dict(obj.get("Author"))
        created = from_datetime(obj.get("Created"))
        is_favorite = from_bool(obj.get("IsFavorite"))
        favorite_count = from_int(obj.get("FavoriteCount"))
        hidden = from_bool(obj.get("Hidden"))
        active = from_bool(obj.get("Active"))
        comment_count = from_int(obj.get("CommentCount"))
        comment_summary = from_union(
            [from_none, CommentSummary.from_dict], obj.get("CommentSummary")
        )
        last_updated = from_union([from_none, from_datetime], obj.get("LastUpdated"))
        avatar_url = from_union([from_none, from_str], obj.get("AvatarUrl"))
        media = from_union(
            [from_none, lambda x: from_list(from_str, x)], obj.get("Media")
        )
        return Entry(
            id,
            content,
            author,
            created,
            is_favorite,
            favorite_count,
            hidden,
            active,
            comment_count,
            comment_summary,
            last_updated,
            avatar_url,
            media,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_int(self.id)
        result["Content"] = from_str(self.content)
        result["Author"] = to_class(UserIdentifier, self.author)
        result["Created"] = self.created.isoformat()
        result["IsFavorite"] = from_bool(self.is_favorite)
        result["FavoriteCount"] = from_int(self.favorite_count)
        result["Hidden"] = from_bool(self.hidden)
        result["Active"] = from_bool(self.active)
        result["CommentCount"] = from_int(self.comment_count)
        result["CommentSummary"] = from_union(
            [from_none, lambda x: to_class(CommentSummary, x)], self.comment_summary
        )
        result["LastUpdated"] = from_union(
            [from_none, lambda x: x.isoformat()], self.last_updated
        )
        result["AvatarUrl"] = from_union([from_none, from_str], self.avatar_url)
        result["Media"] = from_union(
            [from_none, lambda x: from_list(from_str, x)], self.media
        )
        return result
