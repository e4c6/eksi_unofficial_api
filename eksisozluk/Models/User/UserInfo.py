from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any

from eksisozluk.Models import from_int, from_datetime, from_bool, from_none, from_union, from_str, to_class
from eksisozluk.Models.User.CursePeriod import CursePeriod
from eksisozluk.Models.User.Karma import Karma
from eksisozluk.Models.User.UserIdentifier import UserIdentifier
from eksisozluk.Models.User.UserInfoEntryCounts import UserInfoEntryCounts


@dataclass
class UserInfo:
    user_identifier: UserIdentifier
    remaining_invitation: int
    entry_counts: UserInfoEntryCounts
    last_entry_date: datetime
    standing_queue_number: int
    has_any_pending_invitation: bool
    is_buddy: bool
    is_blocked: bool
    is_followed: bool
    is_corporate: bool
    is_deactivated: bool
    is_karma_shown: bool
    is_caylak: bool
    is_index_titles_blocked: bool
    note: None
    is_cursed: bool
    is_banned: bool
    display_twitter_profile: bool
    display_facebook_profile: bool
    display_instagram_profile: bool
    twitter_screen_name: Optional[str] = None
    facebook_profile_url: Optional[str] = None
    facebook_screen_name: Optional[str] = None
    instagram_screen_name: Optional[str] = None
    instagram_profile_url: Optional[str] = None
    karma: Optional[Karma] = None
    curse_period: Optional[CursePeriod] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserInfo':
        assert isinstance(obj, dict)
        user_identifier = UserIdentifier.from_dict(obj.get("UserIdentifier"))
        remaining_invitation = from_int(obj.get("RemainingInvitation"))
        entry_counts = UserInfoEntryCounts.from_dict(obj.get("EntryCounts"))
        last_entry_date = from_datetime(obj.get("LastEntryDate"))
        standing_queue_number = from_int(obj.get("StandingQueueNumber"))
        has_any_pending_invitation = from_bool(obj.get("HasAnyPendingInvitation"))
        is_buddy = from_bool(obj.get("IsBuddy"))
        is_blocked = from_bool(obj.get("IsBlocked"))
        is_followed = from_bool(obj.get("IsFollowed"))
        is_corporate = from_bool(obj.get("IsCorporate"))
        is_deactivated = from_bool(obj.get("IsDeactivated"))
        is_karma_shown = from_bool(obj.get("IsKarmaShown"))
        is_caylak = from_bool(obj.get("IsCaylak"))
        is_index_titles_blocked = from_bool(obj.get("IsIndexTitlesBlocked"))
        note = from_none(obj.get("Note"))
        is_cursed = from_bool(obj.get("IsCursed"))
        is_banned = from_bool(obj.get("IsBanned"))
        display_twitter_profile = from_bool(obj.get("DisplayTwitterProfile"))
        display_facebook_profile = from_bool(obj.get("DisplayFacebookProfile"))
        display_instagram_profile = from_bool(obj.get("DisplayInstagramProfile"))
        twitter_screen_name = from_union([from_none, from_str], obj.get("TwitterScreenName"))
        facebook_profile_url = from_union([from_none, from_str], obj.get("FacebookProfileUrl"))
        facebook_screen_name = from_union([from_none, from_str], obj.get("FacebookScreenName"))
        instagram_screen_name = from_union([from_none, from_str], obj.get("InstagramScreenName"))
        instagram_profile_url = from_union([from_none, from_str], obj.get("InstagramProfileUrl"))
        karma = from_union([from_none, Karma.from_dict], obj.get("Karma"))
        curse_period = from_union([from_none, CursePeriod.from_dict], obj.get("CursePeriod"))
        return UserInfo(user_identifier, remaining_invitation, entry_counts, last_entry_date, standing_queue_number, has_any_pending_invitation, is_buddy, is_blocked, is_followed, is_corporate, is_deactivated, is_karma_shown, is_caylak, is_index_titles_blocked, note, is_cursed, is_banned, display_twitter_profile, display_facebook_profile, display_instagram_profile, twitter_screen_name, facebook_profile_url, facebook_screen_name, instagram_screen_name, instagram_profile_url, karma, curse_period)

    def to_dict(self) -> dict:
        result: dict = {}
        result["UserIdentifier"] = to_class(UserIdentifier, self.user_identifier)
        result["RemainingInvitation"] = from_int(self.remaining_invitation)
        result["EntryCounts"] = to_class(UserInfoEntryCounts, self.entry_counts)
        result["LastEntryDate"] = self.last_entry_date.isoformat()
        result["StandingQueueNumber"] = from_int(self.standing_queue_number)
        result["HasAnyPendingInvitation"] = from_bool(self.has_any_pending_invitation)
        result["IsBuddy"] = from_bool(self.is_buddy)
        result["IsBlocked"] = from_bool(self.is_blocked)
        result["IsFollowed"] = from_bool(self.is_followed)
        result["IsCorporate"] = from_bool(self.is_corporate)
        result["IsDeactivated"] = from_bool(self.is_deactivated)
        result["IsKarmaShown"] = from_bool(self.is_karma_shown)
        result["IsCaylak"] = from_bool(self.is_caylak)
        result["IsIndexTitlesBlocked"] = from_bool(self.is_index_titles_blocked)
        result["Note"] = from_none(self.note)
        result["IsCursed"] = from_bool(self.is_cursed)
        result["IsBanned"] = from_bool(self.is_banned)
        result["DisplayTwitterProfile"] = from_bool(self.display_twitter_profile)
        result["DisplayFacebookProfile"] = from_bool(self.display_facebook_profile)
        result["DisplayInstagramProfile"] = from_bool(self.display_instagram_profile)
        result["TwitterScreenName"] = from_union([from_none, from_str], self.twitter_screen_name)
        result["FacebookProfileUrl"] = from_union([from_none, from_str], self.facebook_profile_url)
        result["FacebookScreenName"] = from_union([from_none, from_str], self.facebook_screen_name)
        result["InstagramScreenName"] = from_union([from_none, from_str], self.instagram_screen_name)
        result["InstagramProfileUrl"] = from_union([from_none, from_str], self.instagram_profile_url)
        result["Karma"] = from_union([from_none, lambda x: to_class(Karma, x)], self.karma)
        result["CursePeriod"] = from_union([from_none, lambda x: to_class(CursePeriod, x)], self.curse_period)
        return result