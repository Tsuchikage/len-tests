from selenium.webdriver.remote.webdriver import WebDriver
import time


class SeleniumFramework:
    """
    Класс-обёртка для работы с Selenium WebDriver.

    Предоставляет базовые методы для открытия страницы и ожидания её полной загрузки.
    """

    def __init__(self, browser: WebDriver, timeout: int = 30):
        """
        Инициализирует фреймворк Selenium.

        :param browser: Экземпляр Selenium WebDriver.
        :param timeout: Время ожидания загрузки страницы в секундах. По умолчанию — 30.
        """
        self.browser = browser
        self.timeout = timeout

    def open_page(self, url: str):
        """
        Открывает страницу по указанному URL.

        :param url: Адрес страницы, которую необходимо открыть.
        :return: None
        """
        self.browser.get(url)

    def wait_until_loaded(self):
        """
        Ожидает полной загрузки страницы.

        :raises TimeoutError: Если страница не загрузилась за отведённое время.
        :return: None
        """
        for _ in range(self.timeout):
            state = self.browser.execute_script("return document.readyState")
            if state == "complete":
                return
            time.sleep(1)
        raise TimeoutError("Страница не загрузилась (document.readyState != 'complete')")
