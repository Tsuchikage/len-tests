from tests.ui.ui_pages.workspace_page import WorkspacePage
from tests.utils.step_logger import StepLogger


class WorkspaceHelperUi:
    """
    Хелпер для взаимодействия со страницей рабочего пространства.
    """

    def __init__(self, browser):
        self.workspace_page = WorkspacePage(browser=browser)

    def create_workspace(self, name: str):
        """
        Создаёт новое рабочее пространство.

        :param name: Имя воркспейса.
        """
        with StepLogger("Нажимаем 'Create a new space'"):
            self.workspace_page.click_create_new_space()

        with StepLogger(f"Вводим имя нового воркспейса '{name}' и нажимаем 'Continue'"):
            self.workspace_page.enter_workspace_name(name)
            self.workspace_page.blur_workspace_input()
            self.workspace_page.click_continue()

    def fill_profile(self, first_name: str, last_name: str, avatar_path: str):
        """
        Заполняет профиль пользователя.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param avatar_path: Путь к аватару.
        """
        with StepLogger("Вводим имя и фамилию"):
            self.workspace_page.enter_first_name(first_name)
            self.workspace_page.enter_last_name(last_name)

        with StepLogger("Загружаем аватарку"):
            self.workspace_page.upload_avatar(avatar_path)

        with StepLogger("Нажимаем 'Continue' после заполнения профиля"):
            self.workspace_page.click_continue()

    def fill_birthday(self, day: str, month: str, year: str):
        """
        Заполняет дату рождения пользователя.

        :param day: День (например, "10").
        :param month: Месяц (например, "May").
        :param year: Год (например, "1995").
        """
        with StepLogger("Устанавливаем дату рождения"):
            self.workspace_page.select_day(day)
            self.workspace_page.select_month(month)
            self.workspace_page.select_year(year)
