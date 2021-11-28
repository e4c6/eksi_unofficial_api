from eksisozluk.Models import *
from datetime import datetime, timedelta


@dataclass
class EksiToken:
    rank: int
    access_token: str
    token_type: str
    expires_in: int
    user_id: Optional[int] = None
    refresh_token: Optional[str] = None
    nick: Optional[str] = None
    issued_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None

    def __post_init__(self):
        self.issued_at = datetime.utcnow()
        self.expires_at = self.issued_at + timedelta(seconds=self.expires_in)

    def is_user(self) -> bool:
        assert(self.is_valid)
        return self.user_id is not None

    def is_valid(self) -> bool:
        return datetime.utcnow() < self.expires_at

    @staticmethod
    def from_dict(obj: Any) -> 'EksiToken':
        assert isinstance(obj, dict)
        rank = int(from_str(obj.get("rank")))
        access_token = from_str(obj.get("access_token"))
        token_type = from_str(obj.get("token_type"))
        expires_in = from_union([from_int, lambda x: int(from_str(x))], obj.get("expires_in"))
        user_id = from_union([from_none, lambda x: int(from_str(x))], obj.get("user_id"))
        refresh_token = from_union([from_str, from_none], obj.get("refresh_token"))
        nick = from_union([from_str, from_none], obj.get("nick"))
        return EksiToken(rank, access_token, token_type, expires_in, user_id, refresh_token, nick)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rank"] = from_str(str(self.rank))
        result["access_token"] = from_str(self.access_token)
        result["token_type"] = from_str(self.token_type)
        result["expires_in"] = from_int(self.expires_in)
        result["user_id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.user_id)
        result["refresh_token"] = from_union([from_str, from_none], self.refresh_token)
        result["nick"] = from_union([from_str, from_none], self.nick)
        return result


