from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional
from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Type, cast, Callable
from datetime import datetime
from enum import Enum
import dateutil.parser

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def parse_date(date_string: str) -> datetime:
    return datetime.strptime(date_string, "%m/%d/%Y %I:%M:%S %p %z")
