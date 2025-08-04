# 📘 Lenza Autotests. Тестовое задание

## 1. Установка окружения

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

pip install -r requirements.txt
````

---

## 2. Запуск всех smoke UI тестов

### Запуск UI автотестов

```bash
pytest -v -m "smoke and ui"
```

### Параллельный запуск в 5 потоков (пройдут быстрее)
```bash
pytest -v -m "smoke and ui" --numprocesses=5
```


### Запуск API автотестов
```bash
pytest -v -m "smoke and api"
```



---

## 3. Структура проекта

```
tests/
├── autotests/
│   ├── api/
│   │   └── smoke/
│   │       └── test_auth_smoke_api.py           # Smoke API-тесты на авторизацию
│   └── ui/
│       └── smoke/
│           ├── auth/                            # Smoke UI-тесты на авторизацию
│           │   ├── negative/                    # Негативные кейсы на авторизацию
│           └── workspace/                       # Smoke UI-тесты на воркспейс и профиль
├── api/
│   ├── api_methods/
│   │   ├── auth_methods_api.py                  # Методы Auth API
│   │   ├── invite_methods_api.py                # Методы Invite API
│   │   └── company_invite_methods_api.py        # Методы Company Invite API
│   └── data/
│       └── auth_data.py                         # Тестовые данные для API
├── ui/
│   ├── data/                                    # Входные данные (email, код и т.д.)
│   ├── ui_helpers/                              # Хелперы с бизнес-логикой действий
│   └── ui_pages/                                # Page Object модели
├── utils/
│   ├── custom_assertions.py                     # Кастомные assert-функции
│   ├── step_logger.py                           # Лог шагов
│   ├── test_logger.py                           # Метаданные тестов
│   └── http_client/                             # Обёртка над requests
├── configuration/                               # Конфиги запуска
├── pytest.ini
└── requirements.txt

```

---

## 4. UI Автотесты

| Тест-кейс                                   | Файл                                                                            |
|---------------------------------------------|---------------------------------------------------------------------------------|
| Авторизация с email и кодом                 | `test_auth_smoke_ui.py::test_enter_email_and_open_code_page`                    |
| Негативная проверка email                   | `test_auth_negative_smoke_ui.py::test_invalid_email_shows_error`                |
| Создание нового воркспейса                  | `test_workspace_smoke_ui.py::test_create_workspace_positive_flow`               |
| Заполнение имени, фамилии, загрузка аватара | `test_workspace_smoke_ui.py::test_fill_profile_with_avatar_and_valid_names`     |
| Установка даты рождения                     | `test_workspace_smoke_ui.py::test_birthday_selection`                           |
| Финальный проверки – welcome message        | `test_workspace_smoke_ui.py::test_final_authorization_check`                    |
| Негативные кейсы (пустой workspace name)    | `test_workspace_profile_negative_smoke_ui.py::test_create_workspace_empty_name` |

## 5. API Автотесты
| Тест-кейс                                                | Файл                                                    |
| -------------------------------------------------------- | ------------------------------------------------------- |
| Авторизация: отправка email и подтверждение кода         | `test_auth_smoke_api.py::test_auth_with_email_and_code` |
| Сквозной кейс: email → код → домен → воркспейс → профиль | `test_auth_smoke_api.py::test_full_auth_cross_case`     |

---
