import pytest

from tests.ui.data.auth_data import AuthData
from tests.ui.data.workspace_data import WorkspaceData
from tests.ui.ui_helpers.auth_helper_ui import AuthHelperUi
from tests.ui.ui_helpers.workspace_helper_ui import WorkspaceHelperUi
from tests.ui.ui_pages.auth_page import AuthPage
from tests.ui.ui_pages.chat_page import ChatPage
from tests.ui.ui_pages.workspace_page import WorkspacePage
from tests.utils.step_logger import StepLogger
from tests.utils.test_logger import TestMetadata
from tests.utils.custom_assertions import assert_true
from tests.utils.ui_settings.browser_settings import wait_seconds


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.workspace
class TestWorkspaceProfileSmokeUi:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.auth_page = AuthPage(browser=browser)
        self.workspace_page = WorkspacePage(browser=browser)
        self.chat_page = ChatPage(browser=browser)

        self.workspace_helper_ui = WorkspaceHelperUi(browser=browser)
        self.auth_helper_ui = AuthHelperUi(browser=browser)

        with StepLogger("Подготавливаем тестовые данные"):
            self.auth_data = AuthData()
            self.workspace_data = WorkspaceData()

        with StepLogger("Открываем страницу авторизации"):
            self.auth_page.open_page()

            with StepLogger("Выполняем авторизацию"):
                self.auth_helper_ui.login_with_code(
                    email=self.auth_data.data.get('email'),
                    code=self.auth_data.data.get('code')
                )

    @TestMetadata(name="Воркспейс: создания нового воркспейса", id="cd807945-2d3a-47f2-be18-0995cf96e9ec")
    def test_create_workspace_positive_flow(self):
        # Act
        with StepLogger("Создаем новое рабочее пространство"):
            self.workspace_page.click_create_new_space()
            self.workspace_page.enter_workspace_name(self.workspace_data.data["workspace_name"])
            self.workspace_page.blur_workspace_input()
            wait_seconds(2)

        with StepLogger("Проверяем, что кнопка Continue активна"):
            assert_true(
                self.workspace_page.is_continue_button_enabled(),
                "Кнопка 'Continue' неактивна при валидном имени."
            )

    @TestMetadata(name="Воркспейс: возврат на экран выбора воркспейсов", id="8c719a51-5a48-4913-9c80-03a2c155c497")
    def test_back_to_workspace_selection(self):
        # Arrange
        with StepLogger("Переходим к созданию нового пространства"):
            self.workspace_page.click_create_new_space()

        # Act
        with StepLogger("Нажимаем кнопку 'Back'"):
            self.workspace_page.click_back()

        # Assert
        with StepLogger("Проверяем, что снова отображается список воркспейсов"):
            assert_true(
                self.workspace_page.is_workspace_list_visible(),
                "Список воркспейсов не отображается после возврата."
            )

    @TestMetadata(name="Профиль: заполнение профиля - имя, фамилия, аватар", id="137351d0-00a1-4f49-b0c6-581d99f1a723")
    def test_fill_profile_with_avatar_and_valid_names(self):
        # Arrange
        with StepLogger("Создаем воркспейс"):
            self.workspace_helper_ui.create_workspace(
                name=self.workspace_data.data.get('workspace_name')
            )

        # Act
        with StepLogger("Заполняем профиль"):
            self.workspace_helper_ui.fill_profile(
                first_name=self.workspace_data.data.get('first_name'),
                last_name=self.workspace_data.data.get('last_name'),
                avatar_path=self.workspace_data.data.get('avatar_path'),
            )

        # Assert
        with StepLogger("Проверяем, что кнопка Continue активна"):
            assert_true(
                self.workspace_page.is_continue_button_enabled_on_profile(),
                "Кнопка 'Continue' неактивна при заполненных полях и аватарке."
            )

    @TestMetadata(name="Профиль: установка даты рождения", id="e6cf866e-c095-47c5-a092-e5e43003dc44")
    def test_birthday_selection(self):
        # Arrange
        with StepLogger("Создаем воркспейс и заполняем профиль"):
            self.workspace_helper_ui.create_workspace(
                name=self.workspace_data.data.get('workspace_name')
            )
            self.workspace_helper_ui.fill_profile(
                first_name=self.workspace_data.data.get('first_name'),
                last_name=self.workspace_data.data.get('last_name'),
                avatar_path=self.workspace_data.data.get('avatar_path'),
            )

        # Act
        with StepLogger("Устанавливаем дату рождения"):
            self.workspace_helper_ui.fill_birthday(day="10", month="May", year="1995")

        # Assert
        with StepLogger("Проверяем, что кнопка Continue активна"):
            assert_true(
                self.workspace_page.is_continue_button_enabled(),
                "Кнопка 'Continue' неактивна при выборе даты."
            )

    @TestMetadata(name="Финальный экран: валидация профиля", id="bde0982b-dff7-476f-ad30-2a574096ec4c")
    def test_final_authorization_check(self):
        # Arrange
        with StepLogger("Создаем воркспейс и заполняем профиль"):
            self.workspace_helper_ui.create_workspace(
                name=self.workspace_data.data.get('workspace_name')
            )
            self.workspace_helper_ui.fill_profile(
                first_name=self.workspace_data.data.get('first_name'),
                last_name=self.workspace_data.data.get('last_name'),
                avatar_path=self.workspace_data.data.get('avatar_path'),
            )

        with StepLogger("Устанавливаем дату рождения"):
            self.workspace_helper_ui.fill_birthday(day="10", month="May", year="1995")

        with StepLogger("Нажимаем 'Continue' после заполнения даты"):
            self.workspace_page.click_continue()

        with StepLogger("Нажимаем 'Invite later'"):
            self.workspace_page.click_invite_later()

        # Assert
        with StepLogger("Проверяем наличие приветственного окна"):
            assert_true(
                self.workspace_page.is_welcome_message_visible(),
                "Приветственное окно не отображается."
            )
