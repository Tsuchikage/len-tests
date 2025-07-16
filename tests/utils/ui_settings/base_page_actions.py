from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class ElementActions:
    """
    Утилитный класс для обёртки часто используемых действий с элементами в Selenium.
    """

    def __init__(self, browser):
        """
        Инициализирует объект действий с элементами.

        :param browser: Экземпляр Selenium WebDriver.
        """
        self.browser = browser

    def _ensure_xpath(self, locator):
        """
        Преобразует строковый локатор в кортеж (By.XPATH, value), если необходимо.

        :param locator: Строка или кортеж локатора.
        :return: Кортеж с методом поиска и значением.
        """
        return (By.XPATH, locator) if isinstance(locator, str) else locator

    def wait_for_element(self, locator, timeout=10):
        """
        Ожидает появления элемента в DOM.

        :param locator: XPath или кортеж локатора.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Найденный WebElement.
        """
        locator = self._ensure_xpath(locator)
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_until_visible(self, locator, timeout=10):
        """
        Ожидает, что элемент станет видимым.

        :param locator: XPath или кортеж локатора.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Видимый WebElement.
        """
        locator = self._ensure_xpath(locator)
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        """
        Ожидает появления элемента и кликает по нему.

        :param locator: XPath или кортеж локатора.
        :param timeout: Максимальное время ожидания в секундах.
        """
        element = self.wait_for_element(locator, timeout)
        element.click()

    def fill_input(self, locator, value, timeout=10):
        """
        Заполняет поле ввода указанным значением.

        :param locator: XPath или кортеж локатора.
        :param value: Значение, которое нужно ввести.
        :param timeout: Максимальное время ожидания в секундах.
        """
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator, timeout=10):
        """
        Получает текст элемента.

        :param locator: XPath или кортеж локатора.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Строка с текстом элемента.
        """
        element = self.wait_for_element(locator, timeout)
        return element.text

    def is_visible(self, locator, timeout=10):
        """
        Проверяет, виден ли элемент.

        :param locator: XPath или кортеж локатора.
        :param timeout: Максимальное время ожидания в секундах.
        :return: True, если элемент виден, иначе False.
        """
        try:
            self.wait_until_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def wait_text_to_be_present_in_element(self, locator, expected_text: str, timeout: int = 10) -> bool:
        """
        Ожидает, что текст элемента станет равен ожидаемому значению.

        :param locator: XPath или кортеж локатора.
        :param expected_text: Текст, который должен появиться.
        :param timeout: Максимальное время ожидания в секундах.
        :return: True, если текст стал ожидаемым, иначе выбрасывает исключение.
        """
        locator = self._ensure_xpath(locator)
        return WebDriverWait(self.browser, timeout).until(
            EC.text_to_be_present_in_element(locator, expected_text)
        )

    def find_elements(self, locator, timeout=10):
        """
        Ищет все элементы, соответствующие локатору.

        :param locator: XPath или кортеж локатора.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Список WebElement'ов.
        """
        locator = self._ensure_xpath(locator)
        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.browser.find_elements(*locator)


    def wait_until_clickable(self, locator, timeout=10):
        """
        Ожидает, что элемент станет кликабельным.

        :param locator: XPath или кортеж локатора.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Элемент, если он становится кликабельным.
        """
        locator = self._ensure_xpath(locator)
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_elements(self, locator, timeout=10):
        """
        Ожидает появления **всех** элементов, соответствующих локатору.

        :param locator: XPath или кортеж локатора.
        :param timeout: Максимальное время ожидания.
        :return: Список найденных WebElement.
        """
        locator = self._ensure_xpath(locator)
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def scroll_to_element(self, locator, timeout=5, by=By.XPATH):
        """
        Выполняет скролл до элемента на странице.
        """
        locator = (by, locator) if isinstance(locator, str) else locator
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = self.browser.find_element(*locator)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def is_enabled(self, locator, timeout=10) -> bool:
        """
        Проверяет, активен ли элемент (доступен ли для взаимодействия).

        :param locator: XPath или кортеж локатора.
        :param timeout: Максимальное время ожидания.
        :return: True, если элемент доступен.
        """
        try:
            element = self.wait_for_element(locator, timeout)
            return element.is_enabled()
        except TimeoutException:
            return False

    def select_by_value(self, locator, value: str, timeout: int = 10) -> None:
        """
        Выбирает значение из выпадающего списка по атрибуту `value`.

        :param locator: XPath или кортеж локатора.
        :param value: Значение атрибута `value`, которое нужно выбрать.
        :param timeout: Максимальное время ожидания в секундах.
        :return: None
        """
        element = self.wait_until_visible(locator, timeout)
        select = Select(element)
        select.select_by_value(value)

    def select_by_visible_text(self, locator, text: str, timeout: int = 10) -> None:
        """
        Выбирает значение из выпадающего списка по отображаемому тексту.

        :param locator: XPath или кортеж локатора.
        :param text: Отображаемый текст, который нужно выбрать.
        :param timeout: Максимальное время ожидания в секундах.
        :return: None
        """
        element = self.wait_until_visible(locator, timeout)
        select = Select(element)
        select.select_by_visible_text(text)

    def click_by_text(self, tag: str, text: str, timeout=10):
        """
        Кликает по элементу, найденному по тексту.

        :param tag: HTML-тег (например, div, span).
        :param text: Отображаемый текст.
        """
        xpath = f"//{tag}[normalize-space(text())='{text}']"
        self.click(xpath, timeout)
