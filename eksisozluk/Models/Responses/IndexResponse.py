from eksisozluk.Models.Index.Index import Index
from eksisozluk.Models.__init__ import *


@dataclass
class IndexResponse:
    success: bool
    message: None
    index: Index

    @staticmethod
    def from_dict(obj: Any) -> 'IndexResponse':
        assert isinstance(obj, dict)
        success = from_bool(obj.get("Success"))
        message = from_none(obj.get("Message"))
        data = Index.from_dict(obj.get("Data"))
        return IndexResponse(success, message, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Success"] = from_bool(self.success)
        result["Message"] = from_none(self.message)
        result["Data"] = to_class(Index, self.index)
        return result


def index_response_from_dict(s: Any) -> IndexResponse:
    return IndexResponse.from_dict(s)


def index_response_to_dict(x: IndexResponse) -> Any:
    return to_class(IndexResponse, x)
