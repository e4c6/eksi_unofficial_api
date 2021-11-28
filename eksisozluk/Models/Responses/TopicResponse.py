from eksisozluk.Models.Responses.ResponseMessage import Message
from eksisozluk.Models.Topic.Topic import Topic
from eksisozluk.Models.__init__ import *


@dataclass
class TopicResponse:
    success: Optional[bool] = None
    message: Optional[Message] = None
    topic: Optional[Topic] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TopicResponse':
        assert isinstance(obj, dict)
        success = from_union([from_bool, from_none], obj.get("Success"))
        message = from_union([from_none, Message], obj.get("Message"))
        data = from_union([Topic.from_dict, from_none], obj.get("Data"))
        return TopicResponse(success, message, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Success"] = from_union([from_bool, from_none], self.success)
        result["Message"] = from_union([from_none, lambda x: to_enum(Message, x)], self.message)
        result["Data"] = from_union([lambda x: to_class(Topic, x), from_none], self.topic)
        return result


def topic_response_from_dict(s: Any) -> List[TopicResponse]:
    return from_list(TopicResponse.from_dict, s)


def topic_response_to_dict(x: List[TopicResponse]) -> Any:
    return from_list(lambda x: to_class(TopicResponse, x), x)
