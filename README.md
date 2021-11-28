# Ekşisözlük Unofficial API Documentation - 2021

Version 1 of this documentation has been [deprecated](doc/V1.md).

Version 2 is [documented on Postman](https://documenter.getpostman.com/view/6963920/TzzEoZpq).

The Version 2 collection can be   [![collection](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/6963920-32242d64-126b-4382-8fb1-0501844f107a?action=collection%2Ffork&collection-url=entityId%3D6963920-32242d64-126b-4382-8fb1-0501844f107a%26entityType%3Dcollection%26workspaceId%3De549a4c7-acfa-45b4-8689-4599ee859e9a).

This library is a work in progress, any contribution are welcome.

# EksiSozluk.py

### Installation

```shell
pip install eksisozluk
```

### Usage

```python
from eksisozluk.EksiSozluk import EksiApi

client = EksiApi()  # or EksiApi(username, password)

entry = client.get_entry( < entry_id >)
topic = client.get_topic( < topic_id >, < page >)
author = client.get_user( < user_nick >)
```