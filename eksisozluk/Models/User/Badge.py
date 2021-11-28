from dataclasses import dataclass
from typing import Any

from eksisozluk.Models import from_str, to_enum
from eksisozluk.Models.User.BadgeName import BadgeName


@dataclass
class Badge:
    name: BadgeName
    description: str

    @staticmethod
    def from_dict(obj: Any) -> 'Badge':
        assert isinstance(obj, dict)
        name = BadgeName(obj.get("Name"))
        description = from_str(obj.get("Description"))
        return Badge(name, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = to_enum(BadgeName, self.name)
        result["Description"] = from_str(self.description)
        return result