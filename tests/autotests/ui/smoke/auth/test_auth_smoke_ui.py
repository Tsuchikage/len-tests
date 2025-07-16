import pytest

from tests.ui.data.auth_data import AuthData
from tests.ui.ui_helpers.auth_helper_ui import AuthHelperUi
from tests.ui.ui_pages.auth_page import AuthPage
from tests.utils.custom_assertions import assert_equal, assert_in, assert_true
from tests.utils.step_logger import StepLogger
from tests.utils.test_logger import TestMetadata


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.auth
class TestAuthSmokeUi:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.auth_page = AuthPage(browser=browser)
        self.auth_helper_ui = AuthHelperUi(browser=browser)


        with StepLogger("Подготавливаем тестовые данные"):
            self.auth_data = AuthData()

            with StepLogger("Открываем страницу авторизации"):
                self.auth_page.open_page()

    @pytest.mark.parametrize(
        "country_code, country_name, expected_button_text, index",
        [
            ("en", "English", "Begin", 0),
            ("en-GB", "English", "Begin", 1),
            ("de", "Deutsch", "Beginnen", 0),
            ("es", "Español", "Comenzar", 0),
            ("fr", "Français", "Commencer", 0),
            ("it", "Italiano", "Inizio", 0),
            ("pt", "Português", "Começar", 0),
            ("ru", "Русский", "Начать", 0),
            ("ar", "العربية", "يبدأ", 0),
            ("ja", "日本語", "始める", 0),
            ("cn", "繁體中文", "開始", 0),
            ("ko", "한국어", "시작하다", 0),
            ("hi", "हिन्दी", "शुरू", 0),
        ]
    )
    @TestMetadata(
        name="Авторизация: смена всех языков на первой странице авторизации",
        id="576bebc8-ec5b-4180-91f8-1c73bffbc3fa",
    )
    def test_change_all_languages_auth_page(self, country_code, country_name, expected_button_text, index):
        # Act
        with StepLogger(f"Меняем язык интерфейса на {country_name} (index={index})"):
            self.auth_page.click_switch_language_button()
            self.auth_page.select_language(
                visible_text=country_name,
                expected_button_text=expected_button_text,
                index=index
            )

        # Assert
        with StepLogger(f"Проверяем, что URL содержит '/{country_code}'"):
            current_url = self.auth_page.browser.current_url
            assert_in(f"/{country_code}", current_url)

        with StepLogger(f"Проверяем, что текст кнопки — '{expected_button_text}'"):
            actual_button_text = self.auth_page.get_begin_button_text()
            assert_equal(actual=actual_button_text.strip(), expected=expected_button_text)

    @TestMetadata(
        name="Авторизация: ввод email и отображение поля подтверждения",
        id="4a1df223-ff11-4ff2-b4e2-43c432db4ef0"
    )
    def test_enter_email_and_open_code_page(self):
        # Arrange
        with StepLogger("Выбираем английский язык и нажимаем 'Begin'"):
            self.auth_page.click_switch_language_button()
            self.auth_page.select_language(visible_text="English", expected_button_text="Begin", index=0)
            self.auth_page.click_begin()

        # Act
        with StepLogger("Вводим email 'test@test.com' и нажимаем 'Continue'"):
            self.auth_page.enter_email(email=self.auth_data.data.get('email'))
            self.auth_page.click_continue()

        # Assert
        with StepLogger("Проверяем, что отображается заголовок 'Check your email'"):
            is_visible = self.auth_page.is_check_email_title_visible()
            assert_true(is_visible, "Заголовок 'Check your email' не отображается.")

    @TestMetadata(
        name="Авторизация: ввод кода, возврат и повторная попытка входа",
        id="c7b9e5e3-9ea9-4cce-9345-0c379cf491c7"
    )
    @TestMetadata(
        name="Ввод кода подтверждения, возврат назад, повторный ввод и вход в workspace",
        id="c7b9e5e3-9ea9-4cce-9345-0c379cf491c7"
    )
    def test_enter_code_and_open_workspace_selection(self):
        email = self.auth_data.data.get('email')
        code = self.auth_data.data.get('code')

        # Act
        with StepLogger("Выбираем английский язык и нажимаем 'Begin'"):
            self.auth_page.click_switch_language_button()
            self.auth_page.select_language("English", "Begin", index=0)
            self.auth_page.click_begin()

        with StepLogger("Вводим email и нажимаем 'Continue'"):
            self.auth_page.enter_email(email=email)
            self.auth_page.click_continue()

        with StepLogger("Нажимаем кнопку 'Назад' до ввода кода"):
            self.auth_page.click_back_button()

        # Assert
        with StepLogger("Проверяем, что снова отображается заголовок 'Welcome to Lenza!'"):
            is_welcome_visible = self.auth_page.is_title_welcome_visible()
            assert_true(is_welcome_visible, "Заголовок 'Welcome to Lenza!' не отображается после нажатия 'Назад'.")

        # Act
        with StepLogger("Повторно вводим email и нажимаем 'Continue'"):
            self.auth_page.enter_email(email=email)
            self.auth_page.click_continue()

        with StepLogger("Вводим код и нажимаем 'Continue'"):
            self.auth_page.enter_confirmation_code(code)
            self.auth_page.click_code_continue()

        # Assert
        with StepLogger("Проверяем, что отображается экран 'Selecting a workspace'"):
            is_workspace_visible = self.auth_page.is_workspace_selection_visible()
            assert_true(is_workspace_visible, "Заголовок 'Selecting a workspace' не отображается.")
