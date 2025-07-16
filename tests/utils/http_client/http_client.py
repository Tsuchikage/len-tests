import json
import requests

from tests.utils import utils


class HttpClient:
    """
    REST API клиент с поддержкой авторизации и отчётности по Swagger Coverage.
    """

    def __init__(self, controller_path: str):
        """
        Инициализирует клиент для указанного сервиса.

        :param controller_path: Контроллер, на который будут отправляться запросы.
        """
        self.controller_path = controller_path
        self.base_url = utils.get_controller_url(name=controller_path)
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }


    def _send_request(
        self,
        method: str,
        endpoint_path: str,
        params: dict = None,
        headers: dict = None,
        json_data: json = None,
        data: dict = None,
        files: dict = None
    ) -> requests.Response:
        """
        Внутренний метод для выполнения HTTP-запроса и записи покрытия Swagger (если включено).

        :param method: HTTP-метод (GET, POST и т.д.).
        :param endpoint_path: Путь эндпоинта относительно base_url.
        :return: Объект ответа requests.Response.
        """

        if headers is None:
            headers = self.headers

        with requests.sessions.Session() as session:
            response = session.request(
                method=method,
                url=f"{self.base_url}{endpoint_path}",
                headers=headers,
                params=params,
                json=json_data,
                data=data,
                files=files,
                timeout=20
            )

        return response

    def get(self, path: str, **kwargs) -> requests.Response:
        """Выполняет GET-запрос по указанному пути."""
        return self._send_request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        """Выполняет POST-запрос по указанному пути."""
        return self._send_request("POST", path, **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        """Выполняет PUT-запрос по указанному пути."""
        return self._send_request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        """Выполняет DELETE-запрос по указанному пути."""
        return self._send_request("DELETE", path, **kwargs)

    def patch(self, path: str, **kwargs) -> requests.Response:
        """Выполняет PATCH-запрос по указанному пути."""
        return self._send_request("PATCH", path, **kwargs)
