from eksisozluk.Models.User.User import User
from eksisozluk.Models.__init__ import *


@dataclass
class UserResponse:
    success: bool
    message: None
    user: User

    @staticmethod
    def from_dict(obj: Any) -> 'UserResponse':
        assert isinstance(obj, dict)
        success = from_bool(obj.get("Success"))
        message = from_none(obj.get("Message"))
        data = User.from_dict(obj.get("Data"))
        return UserResponse(success, message, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Success"] = from_bool(self.success)
        result["Message"] = from_none(self.message)
        result["Data"] = to_class(User, self.user)
        return result


def user_response_from_dict(s: Any) -> List[UserResponse]:
    return from_list(UserResponse.from_dict, s)


def user_response_to_dict(x: List[UserResponse]) -> Any:
    return from_list(lambda x: to_class(UserResponse, x), x)
