from tests.utils.ui_settings.base_page import BasePage

class ChatPage(BasePage):
    def __init__(self, browser, input_point="//div[@id='root']"):
        """
        Страница чата.
        """
        super().__init__(browser, input_point)

        self.PAGE_PATH = "https://chat.....com/"

    def open_page(self):
        """
        Открывает страницу чата.
        """
        self.framework.open_page(self.PAGE_PATH)

    def wait_until_loaded(self):
        """
        Ожидает полной загрузки страницы.
        """
        self.framework.wait_until_loaded()

