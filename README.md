# 📘 Lenza UI Autotests

## 1. Установка окружения

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

pip install -r requirements.txt
````

---

## 2. Запуск всех smoke UI тестов

```bash
pytest -v -m "smoke and ui"
```

---

## 3. Структура проекта

```
tests/
├── autotests/
│   └── ui/
│       ├── smoke/
│       │   ├── auth/               # Smoke-тесты на авторизацию
│       │   └── workspace/          # Smoke-тесты на воркспейс и профиль
│       └── data/                   # Входные данные (email, код, имя и т.д.)
├── ui_helpers/                     # Хелперы с бизнес-логикой действий
├── ui_pages/                       # Page Object для UI-страниц
├── utils/
│   ├── ui_settings/                # Настройка браузера и Selenium
│   ├── custom_assertions.py        # Кастомные assert-функции
│   ├── step_logger.py              # Лог шагов
│   └── test_logger.py              # Метаданные тестов (названия, ID)
```

---

## 4. Основные тесты

| Тест-кейс                                   | Файл                                                                            |
|---------------------------------------------|---------------------------------------------------------------------------------|
| Авторизация с email и кодом                 | `test_auth_smoke_ui.py::test_enter_email_and_open_code_page`                    |
| Негативная проверка email                   | `test_auth_negative_smoke_ui.py::test_invalid_email_shows_error`                |
| Создание нового воркспейса                  | `test_workspace_smoke_ui.py::test_create_workspace_positive_flow`               |
| Заполнение имени, фамилии, загрузка аватара | `test_workspace_smoke_ui.py::test_fill_profile_with_avatar_and_valid_names`     |
| Установка даты рождения                     | `test_workspace_smoke_ui.py::test_birthday_selection`                           |
| Финальный проверки – welcome message        | `test_workspace_smoke_ui.py::test_final_authorization_check`                    |
| Негативные кейсы (пустой workspace name)    | `test_workspace_profile_negative_smoke_ui.py::test_create_workspace_empty_name` |

---
