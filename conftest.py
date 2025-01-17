import pytest
from selene.support.shared import browser as driver
from selene.support.shared import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from config import config as settings_config
from core.utils.helpers import get_current_folder, get_driver_path, get_fixtures

mode = "local"
pytest_plugins = get_fixtures()


def pytest_sessionstart():
    disable_warnings(InsecureRequestWarning)


def pytest_addoption(parser):
    parser.addoption("--mode", action="store", default="local")
    parser.addoption("--browser", action="store", default="chrome")


def _create_driver_with_browser_name(
    *, browser_name: str = "chrome", options: webdriver.ChromeOptions
):
    match browser_name:
        case _:
            return webdriver.Chrome(
                service=ChromeService(executable_path=get_driver_path()),
                options=options,
            )


@pytest.fixture(scope="function")
def browser(pytestconfig):
    global mode
    mode = pytestconfig.getoption("mode")
    browser_name = pytestconfig.getoption("browser")
    match browser_name:
        case _:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])

            options.add_experimental_option(
                "prefs",
                {
                    "profile.default_content_setting_values.notifications": 1,
                    "download.default_directory": get_current_folder(folder="files"),
                    "safebrowsing.enabled": True,
                },
            )
    options.add_argument("--disable-features=InsecureDownloadWarnings")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--ignore-certificate-errors-spki-list")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--allow-running-insecure-content")
    settings_config.browser_name = (
        browser_name if browser_name != "chrome" else settings_config.browser_name
    )
    match mode:
        case "headless":
            options.add_argument("--headless")
            config.driver = _create_driver_with_browser_name(
                browser_name=browser_name, options=options
            )
            config.driver.execute_cdp_cmd(
                "Page.setDownloadBehavior",
                {
                    "behavior": "allow",
                    "downloadPath": get_current_folder(folder="files"),
                },
            )
        case _:
            config.driver = _create_driver_with_browser_name(
                browser_name=browser_name, options=options
            )
    config.browser_name = settings_config.browser_name
    config.window_width = settings_config.browser_window_width
    config.window_height = settings_config.browser_window_height
    config.timeout = settings_config.timeout
    config.save_screenshot_on_failure = False
    config.save_page_source_on_failure = False
    yield driver
    driver.close()
    driver.quit()
