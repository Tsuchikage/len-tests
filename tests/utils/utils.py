from urllib.parse import urljoin

from tests.utils.custom_assertions import assert_equal


def get_controller_url(name: str) -> str:
    """
    Формирует URL сервиса на основе базового адреса API и имени контроллера.

    :param name: Имя контроллера (например, 'auth', 'pages').
    :return: Полный URL до контроллера.
    """
    base_url = "https://api.lenzaos.com/"
    if not base_url.endswith('/'):
        base_url += '/'
    return urljoin(base_url, name)


def check_response_status(response, expected_status: int):
    """
    Проверяет, что статус-код ответа соответствует ожидаемому.

    :param response: Объект ответа (requests.Response).
    :param expected_status: Ожидаемый HTTP-статус.
    :raises Exception: Если статус отличается от ожидаемого.
    """
    if response.status_code != expected_status:
        raise Exception(
            f"Ожидался статус {expected_status}, но получен {response.status_code}. Ответ: {str(response.text)}"
        )


def verify_data(
    actual_data,
    expected_data,
    verified_fields: list = None,
    unverified_fields: list = None,
    msg_option: str = ""
):
    """
    Проверяет соответствие фактических и ожидаемых данных (словарей или списков).

    :param actual_data: Фактические данные (dict или list).
    :param expected_data: Ожидаемые данные (dict или list).
    :param verified_fields: Список ключей, которые нужно проверять (для словаря).
    :param unverified_fields: Список ключей, которые не нужно проверять (для словаря).
    :param msg_option: Доп. сообщение в логах/ошибках.
    :raises AssertionError: Если данные не совпадают.
    :raises TypeError: Если типы данных неподдерживаемые или не совпадают.
    """
    if isinstance(expected_data, dict) and isinstance(actual_data, dict):
        verified_keys = expected_data.keys()
        if verified_fields is not None:
            verified_keys = verified_fields
        elif unverified_fields is not None:
            verified_keys = set(expected_data.keys()) - set(unverified_fields)

        for key in verified_keys:
            actual_value = actual_data.get(key)
            expected_value = expected_data.get(key)
            assert_equal(
                actual_value,
                expected_value,
                f"Ошибка! Несовпадение поля '{key}' {msg_option}.\n"
                f"Фактическое значение: '{actual_value}', Ожидаемое: '{expected_value}'."
            )

    elif isinstance(expected_data, list) and isinstance(actual_data, list):
        assert_equal(
            len(actual_data),
            len(expected_data),
            f"Ошибка! Длина списков не совпадает {msg_option}.\n"
            f"Факт: {len(actual_data)}, Ожидалось: {len(expected_data)}."
        )

        for index, (actual_item, expected_item) in enumerate(zip(actual_data, expected_data)):
            assert_equal(
                actual_item,
                expected_item,
                f"Ошибка! Элемент списка не совпадает по индексу {index} {msg_option}.\n"
                f"Факт: {actual_item}, Ожидалось: {expected_item}."
            )

    else:
        raise TypeError(
            f"Неподдерживаемые или несовпадающие типы данных {msg_option}.\n"
            f"Факт: {type(actual_data)}, Ожидалось: {type(expected_data)}."
        )

    print("Проверка данных прошла успешно.")


def verify_entity_count(
    actual_data,
    expected_count: int,
    msg_option: str = ""
):
    """
    Проверяет, что количество объектов в списке соответствует ожидаемому.

    :param actual_data: Список сущностей.
    :param expected_count: Ожидаемое количество элементов.
    :param msg_option: Доп. сообщение для контекста ошибки.
    :raises AssertionError: Если количество элементов не совпадает.
    """
    if not isinstance(actual_data, list):
        raise TypeError(
            f"Ошибка! Ожидался список для проверки количества {msg_option}.\n"
            f"Тип: {type(actual_data)}."
        )

    actual_count = len(actual_data)
    assert_equal(
        actual_count,
        expected_count,
        f"Ошибка! Количество сущностей не совпадает {msg_option}.\n"
        f"Факт: {actual_count}, Ожидалось: {expected_count}."
    )

    print(f"Проверка количества прошла успешно. Факт: {actual_count}, Ожидалось: {expected_count}.")
