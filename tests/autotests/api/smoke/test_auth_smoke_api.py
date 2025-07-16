import pytest
import random
import string
from tests.api.api_methods.auth_methods_api import AuthApi
from tests.api.api_methods.company_invite_methods_api import CompanyInviteApi
from tests.api.api_methods.invite_methods_api import InviteApi
from tests.api.data.auth_data import AuthData
from tests.utils.step_logger import StepLogger
from tests.utils.test_logger import TestMetadata
from tests.utils.utils import check_response_status


@pytest.mark.api
@pytest.mark.auth
@pytest.mark.smoke
class TestAuthApi:
    """
    Тесты на авторизацию по API.
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        self.auth_api = AuthApi()
        self.company_invite_api = CompanyInviteApi()
        self.invite_api = InviteApi()
        self.auth_data = AuthData()

    @TestMetadata(
        name="Авторизация: отправка email и подтверждение кода",
        id="b0ee5fa2-861c-4f4f-9d5d-5c002c9faabc"
    )
    def test_auth_with_email_and_code(self):
        # Act
        with StepLogger("Отправляем email через POST"):
            response_email = self.auth_api.post_email(email=self.auth_data.data.get('email'))

        with StepLogger("Подтверждаем код через PUT"):
            response_code = self.auth_api.put_code(data=self.auth_data.data)

        # Assert
        with StepLogger("Проверяем статус код ввода email"):
            check_response_status(response_email, 200)

        with StepLogger("Проверяем статус код ввода code"):
            check_response_status(response_code, 200)


    @TestMetadata(
        name="Сквозной тест авторизации",
        id="14c4204e-3a33-492f-9e37-5142f38f58e6"
    )
    def test_full_auth_cross_case(self):
        # Arrange
        domain = "autotest_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        email = self.auth_data.email
        auth_payload = self.auth_data.data

        # Act
        with StepLogger("Отправляем email для начала авторизации (POST /code)"):
            response_email = self.auth_api.post_email(email=email)

        with StepLogger("Подтверждаем код (PUT /code)"):
            response_code = self.auth_api.put_code(data=auth_payload)

        with StepLogger("Получаем hash_code из ответа (PUT /code)"):
            hash_code = response_code.json().get("response").get('hash_code')

        with StepLogger("Проверяем доступность домена (GET /{hash_code}/domain)"):
            response_check_domain = self.auth_api.get_domain_check(hash_code=hash_code, domain=domain)

        with StepLogger("Создаём воркспейс (POST /{hash_code}/new)"):
            response_create_workspace = self.auth_api.post_create_workspace(hash_code=hash_code, domain=domain)

        with StepLogger("Получаем токен приглашения из ответа на создание воркспейса"):
            invite_token = response_create_workspace.json().get("token")

        with StepLogger("Заполняем профиль пользователя (PUT /invite/{token})"):
            response_fill_profile = self.invite_api.put_fill_profile(invite_token=invite_token)

        # Assert
        with StepLogger("Проверяем статус-коды всех этапов"):
            check_response_status(response_email, 200)
            check_response_status(response_code, 200)
            check_response_status(response_check_domain, 200)
            check_response_status(response_create_workspace, 200)
            check_response_status(response_fill_profile, 200)

