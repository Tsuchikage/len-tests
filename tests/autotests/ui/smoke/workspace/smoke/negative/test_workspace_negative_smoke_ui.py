import pytest

from tests.ui.data.auth_data import AuthData
from tests.ui.ui_helpers.auth_helper_ui import AuthHelperUi
from tests.ui.ui_pages.auth_page import AuthPage
from tests.ui.ui_pages.workspace_page import WorkspacePage
from tests.utils.step_logger import StepLogger
from tests.utils.test_logger import TestMetadata
from tests.utils.custom_assertions import assert_true
from tests.utils.ui_settings.browser_settings import wait_seconds


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.workspace
class TestWorkspaceProfileNegativeSmokeUi:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.auth_page = AuthPage(browser=browser)
        self.auth_helper_ui = AuthHelperUi(browser=browser)
        self.workspace_page = WorkspacePage(browser=browser)

        with StepLogger("Подготавливаем тестовые данные"):
            self.auth_data = AuthData()

        with StepLogger("Открываем страницу авторизации"):
            self.auth_page.open_page()

    @TestMetadata(name="Негативный кейс: пустое имя воркспейса", id="2a6c2a29-b152-4d34-878c-b43960c23352")
    def test_create_workspace_empty_name(self):
        # Act
        with StepLogger("Выполняем авторизацию до экрана выбора воркспейса"):
            self.auth_helper_ui.login_with_code(
                email=self.auth_data.data["email"],
                code=self.auth_data.data["code"]
            )

        with StepLogger("Переходим к созданию нового пространства"):
            self.workspace_page.click_create_new_space()

        with StepLogger("Оставляем поле имени пустым и снимаем фокус"):
            self.workspace_page.enter_workspace_name("")
            self.workspace_page.blur_workspace_input()

            wait_seconds(2)

        # Assert
        with StepLogger("Проверяем, что кнопка Continue неактивна"):
            assert_true(
                not self.workspace_page.is_continue_button_enabled(),
                "Кнопка 'Continue' активна при пустом поле."
            )

