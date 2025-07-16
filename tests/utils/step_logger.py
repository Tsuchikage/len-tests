import logging

# Убираем слово "INFO" из логов
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)


class StepLogger:
    """
    Вспомогательный класс для логирования шагов в тестах.

    Логи выводятся в понятном формате, что упрощает отслеживание
    последовательности действий во время выполнения теста.
    """

    def __init__(self, step_message: str):
        """
        Инициализация логгера с сообщением о текущем шаге.

        :param step_message: Описание выполняемого шага.
        """
        self.step_message = step_message

    def __enter__(self):
        """
        Логирует сообщение при входе в контекст.

        :return: self
        """
        logger.info(f"{self.step_message}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Логирует сообщение об ошибке, если при выходе из контекста произошло исключение.

        :param exc_type: Тип исключения (если есть).
        :param exc_value: Значение исключения (если есть).
        :param traceback: Трассировка исключения (если есть).
        :return: False (исключения продолжают распространяться).
        """
        if exc_type is None:
            pass  # Дополнительный лог не требуется при успешном выполнении
        else:
            logger.error(f"ОШИБКА на шаге: {self.step_message}")
        return False


def step(step_message: str):
    """
    Декоратор для логирования шагов в тестах.

    :param step_message: Сообщение, описывающее шаг.
    :return: Обёртка вокруг декорируемой функции с логированием.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            with StepLogger(step_message):
                return func(*args, **kwargs)
        return wrapper
    return decorator
