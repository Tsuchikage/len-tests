import os

from tests.utils.ui_settings.base_page import BasePage
from tests.utils.ui_settings.browser_settings import wait_seconds


class WorkspacePage(BasePage):
    """
    Страница выбора или создания нового рабочего пространства.
    """

    def __init__(self, browser, input_point="//div[@class='p_main']"):
        super().__init__(browser, input_point)

        self.locator_create_new_space = f"{self.input_point}//span[text()='Create a new space']"
        self.locator_workspace_name_input = "//input[@placeholder='Specify a workspace name']"
        self.locator_continue_button = "//button//span[text()='Continue']/.."
        self.locator_back_button = "//p[text()='Back']"
        self.locator_title = "//h2[text()='Specify a workspace name']"

        self.locator_profile_title = "//h2[text()='Set up your personal profile']"
        self.locator_birthday_title = "//h2[contains(text(),'your birthday')]"

        self.locator_day_select = "//select[@name='day']"
        self.locator_month_select = "//select[@name='month']"
        self.locator_year_select = "//select[@name='year']"


    def open_page(self):
        """
        Открывает страницу workspace.
        """
        pass

    def wait_until_loaded(self):
        """
        Ожидает полной загрузки страницы.
        """
        self.framework.wait_until_loaded()

    def click_create_new_space(self) -> None:
        """Кликает по кнопке создания нового пространства."""
        self.actions.wait_until_clickable(self.locator_create_new_space)
        self.actions.click(self.locator_create_new_space)

    def enter_workspace_name(self, name: str) -> None:
        """
        Вводит имя нового воркспейса.

        :param name: Имя рабочего пространства.
        """
        self.actions.fill_input(locator=self.locator_workspace_name_input, value=name)

    def is_continue_button_enabled(self) -> bool:
        """
        Проверяет, активна ли кнопка 'Continue'.

        :return: True, если кнопка активна.
        """
        return self.actions.is_enabled(locator=self.locator_continue_button)

    def is_name_input_visible(self) -> bool:
        """
        Проверяет, отображается ли поле для имени пространства.

        :return: True, если поле видно.
        """
        return self.actions.is_visible(locator=self.locator_workspace_name_input)

    def click_continue(self) -> None:
        """Кликает по кнопке 'Continue'."""
        self.actions.wait_until_clickable(self.locator_continue_button)
        self.actions.click(self.locator_continue_button)
        wait_seconds(2)

    def click_back(self) -> None:
        """Кликает по кнопке 'Back'."""
        self.actions.click(self.locator_back_button)

    def upload_avatar(self, file_path: str) -> None:
        """
        Загружает аватарку по указанному пути.

        :param file_path: Абсолютный или относительный путь к файлу.
        """
        if not os.path.isabs(file_path):
            file_path = os.path.abspath(file_path)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        input_locator = "//input[@type='file']"
        self.browser.find_element("xpath", input_locator).send_keys(file_path)

    def enter_first_name(self, name: str) -> None:
        """
        Вводит имя пользователя.

        :param name: Имя.
        """
        locator = "//input[@placeholder='Enter first name']"
        self.actions.fill_input(locator, name)

    def enter_last_name(self, name: str) -> None:
        """
        Вводит фамилию пользователя.

        :param name: Фамилия.
        """
        locator = "//input[@placeholder='Enter last name']"
        self.actions.fill_input(locator, name)

    def is_continue_button_enabled_on_profile(self) -> bool:
        """
        Проверяет, активна ли кнопка Continue на экране профиля.

        :return: True, если активна.
        """
        return self.actions.is_enabled(self.locator_continue_button)

    def blur_workspace_input(self) -> None:
        """Снимает фокус с инпута для активации валидации."""
        self.actions.click(self.locator_title)

    def is_workspace_list_visible(self) -> bool:
        """
        Проверяет, отображается ли список воркспейсов.

        :return: True, если отображается.
        """
        locator = "//h2[text()='Selecting a workspace']"
        return self.actions.is_visible(locator)

    def is_profile_title_visible(self) -> bool:
        """
        Проверяет, отображается ли заголовок профиля.

        :return: True, если отображается.
        """
        return self.actions.is_visible(self.locator_profile_title)

    def is_birthday_title_visible(self) -> bool:
        """
        Проверяет, отображается ли экран выбора даты рождения.

        :return: True, если отображается.
        """
        return self.actions.is_visible(self.locator_birthday_title)

    def select_custom_dropdown_option(self, label_text: str, value: str) -> None:
        """
        Универсальный метод выбора значения из кастомного dropdown'а.

        :param label_text: Текст label (например: Day, Month, Year).
        :param value: Значение, которое нужно выбрать.
        """
        input_locator = f"//p[.//span[text()='{label_text}']]/ancestor::label//input"
        self.actions.scroll_to_element(locator=input_locator)
        self.actions.click(locator=input_locator)
        wait_seconds(1)

        option_locator = f"//span[contains(@class, 'list-item__title') and normalize-space(text())='{value}']"

        self.actions.scroll_to_element(locator=option_locator)
        self.actions.click(locator=option_locator)

    def select_day(self, day: str) -> None:
        self.select_custom_dropdown_option("Day", day)

    def select_month(self, month: str) -> None:
        self.select_custom_dropdown_option("Month", month)

    def select_year(self, year: str) -> None:
        self.select_custom_dropdown_option("Year", year)

    def is_welcome_message_visible(self) -> bool:
        """
        Проверяет, отображается ли финальное приветственное сообщение после заполнения профиля.

        :return: True, если сообщение отображается.
        """
        locator = "//p[contains(text(), 'Video for owners and admins')]"
        return self.actions.is_visible(locator=locator)

    def click_invite_later(self) -> None:
        """
        Кликает по ссылке 'Invite later' на экране приглашения.
        """
        locator = "//p[contains(@class, 'inu_invite__link_skip') and text()='Invite later']"
        self.actions.wait_until_visible(locator=locator, timeout=10)
        self.actions.scroll_to_element(locator=locator)
        self.actions.wait_until_clickable(locator=locator, timeout=10)
        self.actions.click(locator=locator)

