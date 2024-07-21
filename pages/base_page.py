from time import sleep

from selene import Browser, command, have

from config import config
from core.utils.helpers import get_current_folder


class BaseLocators:
    pass


class BasePage:
    """
    CORE
    """

    def __init__(self, browser: Browser) -> None:
        self.driver: Browser = browser
        self.element = self.driver.element
        self.elements = self.driver.all

    def _click(self, xpath: str, is_js: bool, base_wait: int = 0.3) -> None:
        if is_js:
            self.element(xpath).perform(command=command.js.click)
        else:
            self.element(xpath).click()
        sleep(base_wait)

    """
    BASE METHODS
    """

    def open(self, url: str = "/"):
        self.driver.open(f"{config.ym.url}{url}")

    def save_screenshot(self, filename: str = "screenshot"):
        self.driver.driver.save_screenshot(
            filename=f"{get_current_folder(folder='files')}/{filename}.png"
        )

    def check_text(self, text: str | list, element: str = "//body"):
        if not isinstance(text, list):
            text = [text]
        for item in text:
            self.element(element).should(have.text(item))

    """
    Any
    """

    def click_any_text(self, text: str, idx: int = 1, js_click: bool = False):
        self._click(xpath=f'(//*[text() = "{text}"])[{idx}]', is_js=js_click)

    def click_any_parent_text(self, text: str, idx: int = 1, js_click: bool = False):
        self._click(xpath=f'(//*[text() = "{text}"]/..)[{idx}]', is_js=js_click)

    def click_any_contains_text(self, text: str, idx: int = 1, js_click: bool = False):
        self._click(xpath=f'(//*[contains(text(), "{text}")])[{idx}]', is_js=js_click)

    def click_any_contains_parent_text(
        self, text: str, idx: int = 1, js_click: bool = False
    ):
        self._click(
            xpath=f'(//*[contains(text(), "{text}")]/..)[{idx}]', is_js=js_click
        )

    """
    A
    """

    def click_a_text(self, text: str, idx: int = 1, js_click: bool = False):
        self._click(xpath=f'(//a[text() = "{text}"])[{idx}]', is_js=js_click)
