class AuthData:
    """
    Вспомогательный класс для генерации данных авторизации.
    """

    def __init__(self, email: str = "test@test.com", code: str = "666555"):
        """
        :param email: Email для авторизации (по умолчанию test@test.com).
        :param code: Код подтверждения (по умолчанию 666555).
        """
        self.email = email
        self.code = code

        self.data = {
            "email": self.email,
            "code": self.code,
        }
