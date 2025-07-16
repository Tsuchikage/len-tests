import requests

from tests.utils.http_client.http_client import HttpClient


class AuthApi:
    """
    Клиент для взаимодействия с Auth API.
    """

    def __init__(self):
        self.http_client = HttpClient(controller_path="login")

    def post_email(self, email: str) -> requests.Response:
        """
        Отправляет POST-запрос для начала авторизации по email.

        Endpoint: POST /api/auth/email

        :param email: Email-адрес пользователя.
        :return: Ответ сервера (Response).
        """
        return self.http_client.post(
            path="/code",
            json_data={"email": email}
        )

    def put_code(self, data: dict) -> requests.Response:
        """
        Отправляет PUT-запрос для подтверждения кода авторизации.

        Endpoint: PUT /api/auth/code

        :param data: Данные пользвателя.
        :return: Ответ сервера (Response).
        """
        return self.http_client.put(
            path="/code",
            json_data=data
        )

    def get_domain_check(self, hash_code: str, domain: str) -> requests.Response:
        """
        GET /login/{hash_code}/domain?domain=... — проверка доступности домена.
        """
        return self.http_client.get(
            path=f"/{hash_code}/domain",
            params={"domain": domain}
        )

    def post_create_workspace(self, hash_code: str, domain: str, lang: str = "LANG_4") -> requests.Response:
        """
        POST /login/{hash_code}/new — создание нового воркспейса.
        """
        return self.http_client.post(
            path=f"/{hash_code}/new",
            json_data={
                "domain": domain,
                "description": "",
                "lang": lang
            }
        )