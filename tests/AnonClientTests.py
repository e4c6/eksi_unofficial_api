import pytest

from eksisozluk.EksiSozluk import EksiApi

api = None


@pytest.mark.dependency()
def test_anon_client():
    global api
    api = EksiApi()
    assert api.token is not None


@pytest.mark.dependency(depends=['test_anon_client'])
def test_anon_client_get_entry():
    global api
    entry = api.get_entry(1)
    assert (entry.id == 1)


@pytest.mark.dependency(depends=['test_anon_client'])
def test_anon_client_get_topic():
    global api
    topic = api.get_topic(7006370)
    assert topic.success


@pytest.mark.dependency(depends=['test_anon_client'])
def test_anon_client_get_user():
    user = api.get_user("nimzo")
    assert user.user_info.user_identifier.nick == "nimzo"
