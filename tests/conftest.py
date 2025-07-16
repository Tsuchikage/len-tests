import os

from dotenv import dotenv_values

env_vars = dotenv_values("./configuration/example.env")
for key, value in env_vars.items():
    os.environ.setdefault(key, value)

import pytest

from tests.utils.ui_settings.browser_settings import get_browser

@pytest.fixture
def browser():
    browser = get_browser()
    yield browser
    browser.quit()


