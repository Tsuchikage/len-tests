from tests.ui.ui_pages.auth_page import AuthPage
from tests.ui.ui_pages.workspace_page import WorkspacePage
from tests.utils.step_logger import StepLogger

class AuthHelperUi:
    """
    Хелпер для взаимодействия со страницей авторизации.
    """

    def __init__(self, browser):
        self.auth_page = AuthPage(browser=browser)
        self.workspace_page = WorkspacePage(browser=browser)

    def login_with_code(self, email: str, code: str, click_back_before_code: bool = False):
        """
        Выполняет авторизацию с вводом email и 6-значным кодом.

        :param email: Email для входа.
        :param code: Код подтверждения.
        :param click_back_before_code: Флаг, нужно ли нажимать кнопку "Назад" перед вводом кода, по умолчанию False.
        """
        with StepLogger("Выбираем английский язык и нажимаем 'Begin'"):
            self.auth_page.click_switch_language_button()
            self.auth_page.select_language("English", "Begin", index=0)
            self.auth_page.click_begin()

        with StepLogger(f"Вводим email '{email}' и нажимаем 'Continue'"):
            self.auth_page.enter_email(email)
            self.auth_page.click_continue()

        if click_back_before_code:
            with StepLogger("Нажимаем кнопку 'Назад' после ввода email и возвращаемся к началу"):
                self.auth_page.click_back_button()
                self.auth_page.enter_email(email)
                self.auth_page.click_continue()

        with StepLogger(f"Вводим 6-значный код '{code}'"):
            self.auth_page.enter_confirmation_code(code)
            self.auth_page.click_code_continue()

    def login_and_complete_profile(self, data: dict):
        """
        Выполняет авторизация, создание нового пространства и заполнение профиля.

        :param data: Словарь с данными (email, code, workspace_name, avatar_path, first_name, last_name)
        """
        self.login_with_code(email=data["email"], code=data["code"])

        with StepLogger("Нажимаем 'Create a new space'"):
            self.workspace_page.click_create_new_space()

        with StepLogger(f"Вводим имя нового воркспейса '{data['workspace_name']}' и нажимаем 'Continue'"):
            self.workspace_page.enter_workspace_name(data["workspace_name"])
            self.workspace_page.click_continue()

        with StepLogger("Загружаем аватарку"):
            self.workspace_page.upload_avatar(data["avatar_path"])

        with StepLogger("Вводим имя и фамилию пользователя"):
            self.workspace_page.enter_first_name(data["first_name"])
            self.workspace_page.enter_last_name(data["last_name"])

        with StepLogger("Нажимаем 'Continue' после заполнения профиля"):
            self.workspace_page.click_continue()
