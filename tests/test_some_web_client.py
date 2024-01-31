import responses
import json
import pytest
from some_web_client import SomeResourceClient
from datetime import datetime


# def test_some_resource_client(monkeypatch):
#     # stepik_url = 'https://stepik.org/api/users/37228178'
#     execute_count = 0
#
#     def mock_get_user_status(*args, **kwargs):
#         nonlocal execute_count
#         execute_count += 1
#
#     monkeypatch.setattr('some_web_client.SomeResourceClient.get_user_status', mock_get_user_status)
#
#     stepik_client = SomeResourceClient('https://stepik.org')
#     stepik_client.get_user_info(37228178)

@responses.activate
def test_some_web_client():
    with open('tests/valid_json_answer.json', 'r', encoding='utf-8') as file:
        valid_json_answer = json.load(file)

    responses.add(method=responses.GET, url="https://stepik.org/api/users/37228178", json=valid_json_answer, status=200)
    some_resource_client = SomeResourceClient("https://stepik.org")
    response = some_resource_client.get_user_info(37228178)
    full_name = valid_json_answer["users"][0]["full_name"]
    join_date = datetime.fromisoformat(valid_json_answer["users"][0]["join_date"]).strftime('%d.%m.%Y %H:%M')
    followers_count = valid_json_answer["users"][0]["followers_count"]
    assert response == {"full_name": full_name, "join_date": join_date, 'followers_count': followers_count}


@responses.activate
def test_some_web_client_with_error():
    valid_json_answer_with_error = {
        "detail": "Not found"
    }
    responses.add(method=responses.GET,
                  url="https://stepik.org/api/users/37228178-",
                  json=valid_json_answer_with_error,
                  status=404)
    with pytest.raises(KeyError):
        stepik_client = SomeResourceClient('https://stepik.org')
        stepik_client.get_user_info('37228178-')
