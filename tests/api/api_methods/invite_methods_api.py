import requests

from tests.utils.http_client.http_client import HttpClient


class InviteApi:
    """
    Клиент для взаимодействия с Invite API.
    """

    def __init__(self):
        self.http_client = HttpClient(controller_path="invite")


    def get_invite_info(self, invite_token: str) -> requests.Response:
        """
        GET /invite/{invite_token} — получение информации по приглашению.
        """
        return self.http_client.get(
            path=f"/{invite_token}"
        )

    def put_fill_profile(
        self,
        invite_token: str,
        name: str = "Test",
        surname: str = "User",
        birthday: str = "01-01-1999",
        who_see_birthday: str = "ALL",
        city_id: str = "",
        lang: str = "LANG_4",
        avatar_hash: str = "null"
    ) -> requests.Response:
        """
        PUT /invite/{invite_token}?name=...&surname=... — заполнение профиля пользователя.
        """
        return self.http_client.put(
            path=f"/{invite_token}",
            params={
                "name": name,
                "surname": surname,
                "avatar_hash": avatar_hash,
                "birthday": birthday,
                "who_see_birthday": who_see_birthday,
                "city_id": city_id,
                "lang": lang
            },
            json_data={}  # тело пустое
        )