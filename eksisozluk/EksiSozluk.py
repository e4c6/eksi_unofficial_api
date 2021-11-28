import uuid
import requests
import logging
from eksisozluk.Models.Auth.EksiToken import EksiToken
from eksisozluk.Models.Entry.Entry import Entry
from eksisozluk.Models.Exceptions.ClientException import ClientException
from eksisozluk.Models.Exceptions.EntryNotFoundException import EntryNotFoundException
from eksisozluk.Models.Exceptions.TopicNotFoundException import TopicNotFoundException
from eksisozluk.Models.Exceptions.UserNotFoundException import UserNotFoundException
from eksisozluk.Models.Responses.LoginResponse import LoginResponse
from eksisozluk.Models.Responses.TopicResponse import TopicResponse
from eksisozluk.Models.Responses.ResponseMessage import Message
from eksisozluk.Models.Responses.UserEntriesResponse import UserEntriesResponse
from eksisozluk.Models.Responses.UserResponse import UserResponse
from eksisozluk.Models.Topic.Topic import Topic
from eksisozluk.Models.User.User import User

logging.basicConfig(level=logging.DEBUG)

api = "https://api.eksisozluk.com"
api_secret = "68f779c5-4d39-411a-bd12-cbcc50dc83dd"

routes = {
    "login": "/Token",
    "anon_login": "/v2/account/anonymoustoken",
    "client_info": "/v2/clientsettings/info",
    "topic": "/v2/topic/{}",
    "entry": "/v2/entry/{}",
    "entry_favorite": "/v2/entry/favorite",
    "entry_unfavorite": "/v2/entry/unfavorite",
    "user": "/v2/user/{}",
    "user_follow": "/v2/user/follow",
    "user_unfollow": "/v2/user/unfollow",
    "user_block": "/v2/user/block",
    "user_unblock": "/v2/user/unblock",
    "user_indextitlesblock": "/v2/user/indextitlesblock",
    "user_removeindextitlesblock": "/v2/user/indextitlesblock",
    "user_entries": "/v2/user/{}/entries",
    "user_favorited": "/v2/user/{}/favorited",
    "user_lastvoted": "/v2/user/{}/lastvoted",
    "user_lastweekmostvoted": "/v2/user/{}/lastweekmostvoted",
    "index_popular": "/v2/index/popular",
    "index_today": "/v2/index/today",
    "index_getuserchannelfilters": "/v2/index/getuserchannelfilters",
    "index_setchannelfilter": "/v2/index/setchannelfilter",
}


class EksiApi:
    def __init__(self, username: str = None, password: str = None) -> None:
        self.username = username
        self.password = password
        self.token = None
        self.client_secret = str(uuid.uuid1())
        self.client_unique_id = str(uuid.uuid1())
        self.session = requests.session()
        self.session.hooks = dict(response=self.__hook)
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.DEBUG)
        self.auth()

    def set_session_headers(self):
        self.session.headers["User-agent"] = "okhttp/3.12.1"
        self.session.headers["Authorization"] = "Bearer " + self.token.access_token
        self.session.headers["Client-Secret"] = self.client_secret
        self.session.headers["Api-Secret"] = api_secret

    def get_client_info(self):
        headers = {
            "Client-secret": self.client_secret,
            "Content-type": "application/x-www-form-urlencoded",
            "User-agent": "okhttp/3.12.1"
        }
        payload = {
            "Api-secret": api_secret
        }
        response = requests.post(api + routes["client_info"], headers=headers, data=payload)
        return response.json()

    def __hook(self, res, *args, **kwargs):
        if res.status_code == requests.codes.unauthorized:
            self.__logger.info("Token expired, refreshing")
            self.auth()
            req = res.request
            self.__logger.info("Resending request", req.method, req.url, req.headers)
            req.headers["Authorization"] = self.session.headers["Authorization"]
            return self.session.send(res.request)

    def auth(self):
        if self.username and self.password:
            self.token = self.login(self.username, self.password)
        else:
            self.token = self.anon_login()
        self.__logger.debug("Token: {}".format(self.token))
        self.set_session_headers()

    def anon_login(self) -> EksiToken:
        url = api + routes["anon_login"]
        payload = {
            "Platform": "g",
            "Version": "2.0.0",
            "Build": "51",
            "Api-Secret": api_secret,
            "Client-Secret": self.client_secret,
            "ClientUniqueId": self.client_unique_id
        }
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "User-agent": "okhttp/3.12.1"
        }
        response = requests.post(url, headers=headers, data=payload)
        return LoginResponse.from_dict(response.json()).data

    def login(self, username: str, password: str) -> EksiToken:
        url = api + routes["login"]
        payload = {
            "password": password,
            "Platform": "g",
            "Version": "2.0.0",
            "grant_type": "password",
            "Build": "51",
            "Api-Secret": api_secret,
            "Client-Secret": self.client_secret,
            "ClientUniqueId": self.client_unique_id,
            "username": username
        }
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "User-Agent": "okhttp/3.12.1"
        }
        response = requests.post(url, headers=headers, data=payload)
        return EksiToken.from_dict(response.json())

    def get_entry(self, entry_id: int) -> Entry:
        url = api + routes["entry"].format(entry_id)
        response = self.session.get(url)
        topic_response = TopicResponse.from_dict(response.json())
        if topic_response.message == Message.ENTRY_BULUNAMADI:
            raise EntryNotFoundException("Entry not found")
        return topic_response.topic.get_first_entry()

    def get_topic(self, topic_id: int, page=1) -> TopicResponse:
        url = api + routes["topic"].format(topic_id) + "?p={}".format(page)
        response = self.session.get(url)
        if response.status_code == 200:
            return TopicResponse.from_dict(response.json())
        elif response.status_code == 500:
            raise TopicNotFoundException("Topic not found")
        raise ClientException(f"Unknown error: {response.status_code}")

    def get_user(self, user_nick: str) -> User:
        url = api + routes["user"].format(user_nick)
        response = self.session.get(url)
        if response.status_code == 200:
            user_response = UserResponse.from_dict(response.json())
            return user_response.user
        elif response.status_code == 500:
            raise UserNotFoundException("User not found")
        raise ClientException(f"Unknown error: {response.status_code}")

    def get_user_entries(self, user_nick: str, page=1) -> UserEntriesResponse:
        url = api + routes["user_entries"] + "?p={}".format(page)
        response = self.session.get(url.format(user_nick))
        if response.status_code == 200:
            return UserEntriesResponse.from_dict(response.json())
        raise ClientException(f"Unknown error: {response.status_code}")

    def get_user_favorites(self, user_nick: str, page=1) -> dict:
        url = api + routes["user_favorited"] + "?p={}".format(page)
        response = self.session.get(url.format(user_nick))
        return response.json()

    def get_user_lastvoted(self, user_nick: str, page=1) -> dict:
        url = api + routes["user_lastvoted"] + "?p={}".format(page)
        response = self.session.get(url.format(user_nick))
        return response.json()

    def follow_user(self, user_nick: str) -> dict:
        url = api + routes["user_follow"]
        response = self.session.post(url, data={"user_nick": user_nick})
        return response.json()

    def unfollow_user(self, user_nick: str) -> dict:
        url = api + routes["user_unfollow"]
        response = self.session.post(url, data={"user_nick": user_nick})
        return response.json()

    def block_user(self, user_nick: str) -> dict:
        url = api + routes["user_block"]
        response = self.session.post(url, data={"user_nick": user_nick})
        return response.json()

    def unblock_user(self, user_nick: str) -> dict:
        url = api + routes["user_unblock"]
        response = self.session.post(url, data={"user_nick": user_nick})
        return response.json()

    def get_index_filters(self) -> dict:
        url = api + routes["index_getuserchannelfilters"]
        response = self.session.get(url)
        return response.json()

    def set_index_filter(self, filters: dict) -> dict:
        url = api + routes["index_setchannelfilter"]
        response = self.session.post(url, json=filters)
        return response.json()

    def get_index_popular(self, page=1) -> dict:
        url = api + routes["index_popular"] + "?p={}".format(page)
        response = self.session.get(url)
        return response.json()

    def get_index_today(self, page=1) -> dict:
        url = api + routes["index_today"] + "?p={}".format(page)
        response = self.session.get(url)
        return response.json()

    def favorite_entry(self, entry_id: int) -> dict:
        url = api + routes["entry_favorite"]
        response = self.session.post(url, data={"entry_id": entry_id})
        return response.json()

    def unfavorite_entry(self, entry_id: int) -> dict:
        url = api + routes["entry_unfavorite"]
        response = self.session.delete(url, data={"entry_id": entry_id})
        return response.json()
