from eksisozluk.Models.__init__ import *
from eksisozluk.Models.Auth.EksiToken import EksiToken


@dataclass
class LoginResponse:
    success: Optional[bool]
    data: EksiToken
    message: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LoginResponse':
        assert isinstance(obj, dict)
        success = from_union([from_bool, from_none], obj.get("Success"))
        message = from_union([from_str, from_none], obj.get("Message"))
        data = EksiToken.from_dict(obj.get("Data"))
        return LoginResponse(success, data, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Success"] = from_union([from_bool, from_none], self.success)
        result["Message"] = from_union([from_str, from_none], self.message)
        result["Data"] = to_class(EksiToken, self.data)
        return result


def login_response_from_dict(s: Any) -> LoginResponse:
    return LoginResponse.from_dict(s)


def login_response_to_dict(x: LoginResponse) -> Any:
    return to_class(LoginResponse, x)
