# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = time_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class TimeResponse:
    success: bool
    message: None
    data: int

    @staticmethod
    def from_dict(obj: Any) -> "TimeResponse":
        assert isinstance(obj, dict)
        success = from_bool(obj.get("Success"))
        message = from_none(obj.get("Message"))
        data = from_int(obj.get("Data"))
        return TimeResponse(success, message, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Success"] = from_bool(self.success)
        result["Message"] = from_none(self.message)
        result["Data"] = from_int(self.data)
        return result


def time_response_from_dict(s: Any) -> TimeResponse:
    return TimeResponse.from_dict(s)


def time_response_to_dict(x: TimeResponse) -> Any:
    return to_class(TimeResponse, x)
