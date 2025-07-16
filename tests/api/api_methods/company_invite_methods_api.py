import requests

from tests.utils.http_client.http_client import HttpClient


class CompanyInviteApi:
    """
    Клиент для взаимодействия с CompanyInvite API.
    """

    def __init__(self):
        self.http_client = HttpClient(controller_path="company")


    def get_invite_info(self, invite_token: str) -> requests.Response:
        """
        GET /invite/{invite_token} — получение информации по приглашению.
        """
        return self.http_client.get(
            path=f"/{invite_token}"
        )

    def post_invite_link(self, token: str, count: int = 12) -> requests.Response:
        """
        POST /company/invite/link — генерация ссылки-приглашения.
        """
        headers = {
            "token": token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        return self.http_client.post(
            path="/invite/link",
            json_data={"count": count},
            headers=headers
        )