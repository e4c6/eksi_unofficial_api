from eksisozluk.Models.__init__ import *

@dataclass
class DisplayInfo:
    id: Optional[int] = None
    external_id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    thumb_uri: Optional[str] = None
    big_thumb_uri: Optional[str] = None
    file_uri: Optional[str] = None
    embedded_video_uri: Optional[str] = None
    options: Optional[int] = None
    is_advertorial: Optional[bool] = None
    polls_enabled: Optional[bool] = None
    play_video_in_topic: Optional[bool] = None
    click_to_play: Optional[bool] = None
    has_embedded_video_link: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DisplayInfo':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("Id"))
        external_id = from_union([from_int, from_none], obj.get("ExternalId"))
        title = from_union([from_str, from_none], obj.get("Title"))
        description = from_union([from_str, from_none], obj.get("Description"))
        thumb_uri = from_union([from_str, from_none], obj.get("ThumbUri"))
        big_thumb_uri = from_union([from_str, from_none], obj.get("BigThumbUri"))
        file_uri = from_union([from_str, from_none], obj.get("FileUri"))
        embedded_video_uri = from_union([from_str, from_none], obj.get("EmbeddedVideoUri"))
        options = from_union([from_int, from_none], obj.get("Options"))
        is_advertorial = from_union([from_bool, from_none], obj.get("IsAdvertorial"))
        polls_enabled = from_union([from_bool, from_none], obj.get("PollsEnabled"))
        play_video_in_topic = from_union([from_bool, from_none], obj.get("PlayVideoInTopic"))
        click_to_play = from_union([from_bool, from_none], obj.get("ClickToPlay"))
        has_embedded_video_link = from_union([from_bool, from_none], obj.get("HasEmbeddedVideoLink"))
        return DisplayInfo(id, external_id, title, description, thumb_uri, big_thumb_uri, file_uri, embedded_video_uri, options, is_advertorial, polls_enabled, play_video_in_topic, click_to_play, has_embedded_video_link)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([from_int, from_none], self.id)
        result["ExternalId"] = from_union([from_int, from_none], self.external_id)
        result["Title"] = from_union([from_str, from_none], self.title)
        result["Description"] = from_union([from_str, from_none], self.description)
        result["ThumbUri"] = from_union([from_str, from_none], self.thumb_uri)
        result["BigThumbUri"] = from_union([from_str, from_none], self.big_thumb_uri)
        result["FileUri"] = from_union([from_str, from_none], self.file_uri)
        result["EmbeddedVideoUri"] = from_union([from_str, from_none], self.embedded_video_uri)
        result["Options"] = from_union([from_int, from_none], self.options)
        result["IsAdvertorial"] = from_union([from_bool, from_none], self.is_advertorial)
        result["PollsEnabled"] = from_union([from_bool, from_none], self.polls_enabled)
        result["PlayVideoInTopic"] = from_union([from_bool, from_none], self.play_video_in_topic)
        result["ClickToPlay"] = from_union([from_bool, from_none], self.click_to_play)
        result["HasEmbeddedVideoLink"] = from_union([from_bool, from_none], self.has_embedded_video_link)
        return result


@dataclass
class Video:
    display_info: Optional[DisplayInfo] = None
    in_topic_video: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Video':
        assert isinstance(obj, dict)
        display_info = from_union([DisplayInfo.from_dict, from_none], obj.get("DisplayInfo"))
        in_topic_video = from_union([from_bool, from_none], obj.get("InTopicVideo"))
        return Video(display_info, in_topic_video)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DisplayInfo"] = from_union([lambda x: to_class(DisplayInfo, x), from_none], self.display_info)
        result["InTopicVideo"] = from_union([from_bool, from_none], self.in_topic_video)
        return result