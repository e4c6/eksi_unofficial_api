from dataclasses import dataclass
from typing import Any

from eksisozluk.Models import from_int, to_enum
from eksisozluk.Models.User.KarmaName import KarmaName


@dataclass
class Karma:
    name: KarmaName
    value: int

    @staticmethod
    def from_dict(obj: Any) -> 'Karma':
        assert isinstance(obj, dict)
        name = KarmaName(obj.get("Name"))
        value = from_int(obj.get("Value"))
        return Karma(name, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = to_enum(KarmaName, self.name)
        result["Value"] = from_int(self.value)
        return result