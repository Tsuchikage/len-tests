from tests.utils.ui_settings.base_page import BasePage

class AuthPage(BasePage):
    def __init__(self, browser, input_point="//div[@class='p_main']"):
        """
        Страница авторизации.
        """
        super().__init__(browser, input_point)

        self.PAGE_PATH = "https://auth.....com"

        self.locator_title = f"{self.input_point}//h2[contains(text(), 'Welcome to Lenza!')]"
        self.locator_switch_language_button = f"{self.input_point}//button[contains(@class, 'lang-switch')]"
        self.language_option_icon = "//div[contains(@class, 'list-item')]//span[contains(text(), '{}')]"
        self.locator_begin_button_text = f"{self.input_point}//button[contains(@class, 'button-ui')]//span[@class='btn__title']"

        self.locator_email_input = f"{self.input_point}//input[@id='email-input']"
        self.locator_continue_button = f"{self.input_point}//button[.//span[text()='Continue']]"
        self.locator_check_email_title = f"{self.input_point}//h2[text()='Check your email']"
        self.locator_code_inputs = f"{self.input_point}//input[@class='code-input__field']"
        self.locator_code_continue_button = f"{self.input_point}//button//span[text()='Continue']"
        self.locator_workspace_title = f"{self.input_point}//h2[text()='Selecting a workspace']"

        self.locator_email_error = "//p[contains(text(), 'Invalid email address')]"
        self.locator_code_error = "//p[contains(text(), 'The code is entered incorrectly')]"
        self.locator_continue_disabled_button = "//button[.//span[text()='Continue'] and @disabled]"

        # TODO: SVG-иконка "назад" (<svg class="btn_back">) не обёрнута ни в <button>, ни в <div>, ни в другой интерактивный HTML-элемент.
        #  Не соответствует семантики HTML.
        self.locator_back_arrow = "//*[name()='svg' and contains(@class, 'btn_back')]"

    def open_page(self):
        """
        Открывает страницу авторизации.
        """
        self.framework.open_page(self.PAGE_PATH)

    def wait_until_loaded(self):
        """
        Ожидает полной загрузки страницы.
        """
        self.framework.wait_until_loaded()

    def click_switch_language_button(self):
        """
        Кликает по кнопке выбора языка.
        """
        self.actions.click(locator=self.locator_switch_language_button)

    def select_language(self, visible_text: str, expected_button_text: str, index: int = 0):
        """
        Выбирает язык из выпадающего списка по названию. Учитывает дублирующиеся языки по индексу.

        :param visible_text: Название языка, отображаемое в списке (например, 'English').
        :param expected_button_text: Текст, ожидаемый на кнопке после смены языка.
        :param index: Индекс нужного языка, если их несколько с одинаковым названием.
        :raises ValueError: Если язык не найден.
        :raises IndexError: Если индекс превышает количество найденных языков.
        """
        locator = f"//div[contains(@class, 'list-item')]//span[starts-with(text(), '{visible_text}')]"
        elements = self.actions.find_elements(locator)

        if not elements:
            raise ValueError(f"Не найден ни один элемент с текстом, начинающимся на '{visible_text}'")

        if index >= len(elements):
            raise IndexError(f"Найдено {len(elements)} элементов, но запрошен индекс {index} для '{visible_text}'")

        elements[index].click()

        self.actions.wait_text_to_be_present_in_element(
            locator=self.locator_begin_button_text,
            expected_text=expected_button_text
        )

    def get_begin_button_text(self) -> str:
        """
        Получает текст с кнопки "Начать/Begin/..." на стартовой странице.

        :return: Строка с текстом кнопки.
        """
        return self.actions.get_text(locator=self.locator_begin_button_text)

    def click_begin(self):
        """
        Кликает по кнопке "Начать"/"Begin" на стартовой странице.
        """
        self.actions.click(locator=self.locator_begin_button_text)

    def enter_email(self, email: str):
        """
        Вводит email.

        :param email: Адрес электронной почты для авторизации.
        """
        self.actions.fill_input(locator=self.locator_email_input, value=email)

    def click_continue(self):
        """
        Ожидает кликабельность и кликает по кнопке "Continue" после ввода email.
        """
        self.actions.wait_until_clickable(self.locator_continue_button)
        self.actions.click(locator=self.locator_continue_button)

    def is_check_email_title_visible(self) -> bool:
        """
        Проверяет, отображается ли заголовок после ввода email.

        :return: True, если заголовок видим, иначе False.
        """
        return self.actions.is_visible(locator=self.locator_check_email_title)

    def enter_confirmation_code(self, code: str):
        """
        Вводит 6-значный код подтверждения, отправленный на email.

        :param code: Код подтверждения (например, '666555').
        """
        active_input_locator = "//input[contains(@class, 'code-input__field--current')]"
        active_input = self.actions.wait_for_element(locator=active_input_locator)

        active_input.send_keys(code)

    def click_code_continue(self):
        """
        Кликает по кнопке "Continue" после ввода кода.
        """
        self.actions.click(locator=self.locator_code_continue_button)

    def is_workspace_selection_visible(self) -> bool:
        """
        Проверяет, что отображается экран выбора рабочего пространства.

        :return: True, если экран с заголовком "Selecting a workspace" видим, иначе False.
        """
        return self.actions.is_visible(locator=self.locator_workspace_title)


    def is_invalid_email_error_visible(self) -> bool:
        """
        Проверяет, отображается ли ошибка при вводе некорректного email.
        """
        return self.actions.is_visible(locator=self.locator_email_error)

    def is_invalid_code_error_visible(self) -> bool:
        """
        Проверяет, отображается ли ошибка при вводе неправильного кода.
        """
        return self.actions.is_visible(locator=self.locator_code_error)

    def is_continue_button_disabled(self) -> bool:
        """
        Проверяет, что кнопка Continue неактивна.
        """
        return self.actions.is_visible(locator=self.locator_continue_disabled_button)


    def blur_email_input(self):
        """
        Снимает фокус с поля email, кликнув в пустое место.
        """
        self.actions.click(locator=self.locator_title)

    def click_back_button(self):
        """
        Кликает по иконке "Назад" на экране с вводом кода.
        """
        self.actions.wait_for_element(self.locator_back_arrow)
        self.actions.click(self.locator_back_arrow)

    def is_title_welcome_visible(self) -> bool:
        """
        Проверяет, что отображается заголовок 'Welcome to Lenza!'.
        """
        return self.actions.is_visible(locator=self.locator_title)
