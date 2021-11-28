from dataclasses import dataclass
from typing import Any

from eksisozluk.Models import from_str, from_int


@dataclass
class UserIdentifier:
    nick: str
    id: int

    @staticmethod
    def from_dict(obj: Any) -> 'UserIdentifier':
        assert isinstance(obj, dict)
        nick = from_str(obj.get("Nick"))
        id = from_int(obj.get("Id"))
        return UserIdentifier(nick, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Nick"] = from_str(self.nick)
        result["Id"] = from_int(self.id)
        return result