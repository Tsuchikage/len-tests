import pytest

from tests.ui.ui_pages.auth_page import AuthPage
from tests.utils.custom_assertions import assert_true
from tests.utils.step_logger import StepLogger
from tests.utils.test_logger import TestMetadata


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.auth
@pytest.mark.negative
class TestAuthNegativeSmokeUi:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.auth_page = AuthPage(browser=browser)
        with StepLogger("Открываем страницу авторизации"):
            self.auth_page.open_page()

    @TestMetadata(
        name="Проверка отображения ошибки при невалидном email",
        id="0b8f8f24-8cd3-4e75-9843-57aaffd3cf10"
    )
    def test_invalid_email_shows_error(self):
        with StepLogger("Выбираем язык и нажимаем 'Begin'"):
            self.auth_page.click_switch_language_button()
            self.auth_page.select_language(visible_text="English", expected_button_text="Begin", index=0)
            self.auth_page.click_begin()

        with StepLogger("Вводим некорректный email"):
            self.auth_page.enter_email(email="12312@reww.ce")

        with StepLogger("Снимаем фокус с поля email"):
            self.auth_page.blur_email_input()

        with StepLogger("Проверяем, что отображается ошибка валидации email"):
            is_error_visible = self.auth_page.is_invalid_email_error_visible()
            assert_true(is_error_visible, "Сообщение об ошибке валидации email отсутствует")

        with StepLogger("Проверяем, что кнопка 'Continue' неактивна"):
            is_disabled = self.auth_page.is_continue_button_disabled()
            assert_true(is_disabled, "Кнопка 'Continue' активна при невалидном email")

    @TestMetadata(
        name="Проверка активности кнопки 'Continue' без ввода кода",
        id="f2f827a0-61bc-4d0f-8c24-3f407dff3d3e"
    )
    def test_continue_disabled_without_code(self):
        # Arrange
        with StepLogger("Проходим этап email без ввода кода подтверждения"):
            self.auth_page.click_switch_language_button()
            self.auth_page.select_language(visible_text="English", expected_button_text="Begin", index=0)
            self.auth_page.click_begin()
            self.auth_page.enter_email(email="test@test.com")
            self.auth_page.click_continue()

        # Assert
        with StepLogger("Проверяем, что кнопка 'Continue' неактивна"):
            is_disabled = self.auth_page.is_continue_button_disabled()
            assert_true(is_disabled, "Кнопка 'Continue' активна при пустом коде")
