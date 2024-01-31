import requests
from datetime import datetime


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def get_user_status(self, user_id):
        response = requests.get(f'{self.url}/api/users/{user_id}')
        return response.json()

    def get_user_info(self, user_id):
        json_data = self.get_user_status(user_id)
        full_name = json_data["users"][0]["full_name"]
        join_date = datetime.fromisoformat(json_data["users"][0]["join_date"]).strftime('%d.%m.%Y %H:%M')
        followers_count = json_data["users"][0]["followers_count"]
        return {
            "full_name": full_name,
            "join_date": join_date,
            'followers_count': followers_count
        }


if __name__ == '__main__':
    stepik_client = SomeResourceClient('https://stepik.org')
    print(stepik_client.get_user_info(37228178))