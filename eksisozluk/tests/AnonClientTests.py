import pytest

from eksisozluk.EksiSozluk import EksiApi

api: EksiApi


@pytest.mark.dependency()
def test_anon_client():
    global api
    api = EksiApi()
    assert api.token is not None


@pytest.mark.dependency(depends=['test_anon_client'])
def test_anon_client_get_entry():
    entry = api.get_entry(1)
    assert (entry.id == 1)


@pytest.mark.dependency(depends=['test_anon_client'])
def test_anon_client_get_topic():
    topic = api.get_topic(7006370)
    assert topic.success


@pytest.mark.dependency(depends=['test_anon_client'])
def test_anon_client_get_user():
    user = api.get_user("nimzo")
    assert user.user_info.user_identifier.nick == "nimzo"

@pytest.mark.dependency(depends=['test_anon_client'])
def test_anon_client_get_index_today():
    topic_response = api.get_index_today()
    assert len(topic_response.index.topics) > 0
