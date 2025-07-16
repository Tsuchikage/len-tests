import time

from tests.utils.ui_settings.selenoid.chrome import ChromeBrowserConfig


def get_browser():
    """
    Возвращает настроенный экземпляр WebDriver, используя ChromeBrowserConfig.

    Автоматически выбирает локальный или удалённый режим на основе переменных из .env.

    :return: Экземпляр Selenium WebDriver.
    """
    return ChromeBrowserConfig().run()


def wait_seconds(seconds: int):
    """
    Простая обёртка над time.sleep для повышения читаемости автотестов.

    :param seconds: Количество секунд, на которые нужно приостановить выполнение.
    :return: None
    """
    time.sleep(seconds)
