def assert_equal(actual, expected, message=None):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если значения не равны.
    """
    if actual != expected:
        raise AssertionError(message or f"Ожидалось {expected}, но получено {actual}.")


def assert_not_equal(actual, expected, message=None):
    """
    Проверяет, что фактическое значение не равно ожидаемому.

    :param actual: Фактическое значение.
    :param expected: Значение, которому не должно быть равно.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если значения равны.
    """
    if actual == expected:
        raise AssertionError(message or f"Не ожидалось {expected}, но получено {actual}.")


def assert_true(value, message=None):
    """
    Проверяет, что значение истинно (True).

    :param value: Проверяемое значение.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если значение ложно.
    """
    if not value:
        raise AssertionError(message or f"Ожидалось True, но получено {value}.")


def assert_false(value, message=None):
    """
    Проверяет, что значение ложно (False).

    :param value: Проверяемое значение.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если значение истинно.
    """
    if value:
        raise AssertionError(message or f"Ожидалось False, но получено {value}.")


def assert_is_none(value, message=None):
    """
    Проверяет, что значение является None.

    :param value: Проверяемое значение.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если значение не None.
    """
    if value is not None:
        raise AssertionError(message or f"Ожидалось None, но получено {value}.")


def assert_is_not_none(value, message=None):
    """
    Проверяет, что значение не является None.

    :param value: Проверяемое значение.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если значение является None.
    """
    if value is None:
        raise AssertionError(message or "Ожидалось значение, отличное от None.")


def assert_greater(actual, expected, message=None):
    """
    Проверяет, что фактическое значение больше ожидаемого.

    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение для сравнения.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если фактическое значение не больше ожидаемого.
    """
    if not actual > expected:
        raise AssertionError(message or f"Ожидалось, что {actual} > {expected}.")


def assert_greater_equal(actual, expected, message=None):
    """
    Проверяет, что фактическое значение больше или равно ожидаемому.

    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение для сравнения.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если фактическое значение меньше ожидаемого.
    """
    if not actual >= expected:
        raise AssertionError(message or f"Ожидалось, что {actual} >= {expected}.")


def assert_less(actual, expected, message=None):
    """
    Проверяет, что фактическое значение меньше ожидаемого.

    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение для сравнения.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если фактическое значение не меньше ожидаемого.
    """
    if not actual < expected:
        raise AssertionError(message or f"Ожидалось, что {actual} < {expected}.")


def assert_less_equal(actual, expected, message=None):
    """
    Проверяет, что фактическое значение меньше или равно ожидаемому.

    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение для сравнения.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если фактическое значение больше ожидаемого.
    """
    if not actual <= expected:
        raise AssertionError(message or f"Ожидалось, что {actual} <= {expected}.")


def assert_in(item, container, message=None):
    """
    Проверяет, что элемент присутствует в контейнере.

    :param item: Элемент, наличие которого проверяется.
    :param container: Коллекция, в которой производится поиск.
    :param message: Дополнительное сообщение об ошибке (необязательно).
    :raises AssertionError: Если элемент не найден в контейнере.
    """
    if item not in container:
        raise AssertionError(message or f"Ожидалось, что {item} присутствует в {container}.")
