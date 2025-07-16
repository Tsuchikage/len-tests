from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver

from tests.utils.ui_settings.base_page_actions import ElementActions
from tests.utils.ui_settings.selenium_framework import SeleniumFramework


class BasePage(ABC):
    """
    Абстрактный базовый класс для всех Page Object классов.

    Обеспечивает доступ к WebDriver и общим методам взаимодействия с элементами страницы.
    """

    def __init__(self, browser: WebDriver, input_point: str):
        """
        Инициализирует базовую страницу с экземпляром WebDriver и вспомогательными утилитами.

        :param browser: Экземпляр Selenium WebDriver.
        :param input_point: XPath или другой локатор, определяющий основной контейнер страницы.
        """
        self.browser = browser
        self.input_point = input_point
        self.actions = ElementActions(browser)
        self.framework = SeleniumFramework(browser)

    @abstractmethod
    def open_page(self):
        """
        Абстрактный метод для открытия страницы.

        Должен быть реализован в дочерних классах.
        :return: None
        """
        pass

    @abstractmethod
    def wait_until_loaded(self):
        """
        Абстрактный метод для ожидания полной загрузки страницы.

        Должен быть реализован в дочерних классах.
        :return: None
        """
        pass
