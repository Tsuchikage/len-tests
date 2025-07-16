import functools
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
test_logger = logging.getLogger("TestLogger")


def TestMetadata(name: str, id: str):
    """
    Декоратор для установки метаданных теста (имя и ID) и логирования перед выполнением.

    :param name: Название теста.
    :param id: Уникальный идентификатор теста.
    :return: Обёрнутая функция с логированием метаданных перед запуском.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Логируем метаданные теста перед выполнением
            test_logger.info(f"\nНазвание: {name}\nID: {id}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator
