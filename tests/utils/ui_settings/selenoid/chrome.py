import os
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class ChromeBrowserConfig:
    def __init__(self):
        self.browser = None
        self.launch_mode = os.getenv("WEBDRIVER_LAUNCH_MODE", "local").lower()
        self.browser_version = os.getenv("WEBDRIVER_VERSION", "")
        self.browser_name = os.getenv("WEBDRIVER_BROWSER", "chrome")
        self.selenoid_url = os.getenv("SELENOID_URL", "")
        self._test_name = os.getenv("PYTEST_CURRENT_TEST", "test").split(":")[-1].split(" ")[0]
        self.download_dir = os.getcwd()

    def run(self) -> WebDriver:
        if self.launch_mode == "remote":
            driver = self._remote()
        elif self.launch_mode == "local":
            driver = self._local()
        else:
            raise Exception(f"Unknown launch mode: {self.launch_mode}")

        # Set base_url after driver is created
        driver.base_url = os.getenv("BASE_URL", "")
        return driver

    def _get_common_options(self):
        dt_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        options = webdriver.ChromeOptions()

        prefs = {
            "download.default_directory": self.download_dir,
            "profile.password_manager_leak_detection": False
        }
        options.add_experimental_option("prefs", prefs)
        options.set_capability("browserName", self.browser_name)

        if self.launch_mode == "remote" and self.browser_version:
            options.set_capability("browserVersion", self.browser_version)

        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
        return options, dt_now

    def _remote(self) -> WebDriver:
        options, dt_now = self._get_common_options()

        selenoid_capabilities = {
            "enableVNC": os.getenv("SELENOID_ENABLE_VNC", "true").lower() == "true",
            "enableVideo": os.getenv("SELENOID_ENABLE_VIDEO", "false").lower() == "true",
            "videoName": os.getenv("SELENOID_VIDEO_NAME", "video.mp4"),
            "videoScreenSize": os.getenv("SELENOID_VIDEO_SCREEN_SIZE", "1920x1080"),
            "videoFrameRate": int(os.getenv("SELENOID_VIDEO_FRAME_RATE", "24")),
            "videoCodec": os.getenv("SELENOID_VIDEO_CODEC", "mpeg4"),
            "enableLog": os.getenv("SELENOID_ENABLE_LOG", "true").lower() == "true",
            "logName": f"{self._test_name}_{dt_now}.log",
            "name": self._test_name,
            "labels": {"environment": "UI"},
            "sessionTimeout": os.getenv("SELENOID_SESSION_TIMEOUT", "7m")
        }

        options.set_capability("selenoid:options", selenoid_capabilities)

        executor = f"{self.selenoid_url}/wd/hub"
        return webdriver.Remote(command_executor=executor, options=options)

    def _local(self) -> WebDriver | None:
        options, _ = self._get_common_options()
        service = Service(executable_path=ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=options)
        return self.browser
