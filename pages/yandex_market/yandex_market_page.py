from config import config
from pages import BasePage


class YandexMarketPage(BasePage):
    """
    ЯНДЕКС.МАРКЕТ: Главная
    """

    def auth_yandex_market(self, email: str, password: str):
        self.open()
        self.click_a_text(text="Войти")
        self.check_text(text="Войдите с Яндекс ID")
        self.set_email(email=email)
        self.click_any_parent_text(text="Войти")
        self.set_password(password=password)
        self.click_any_parent_text(text="Продолжить")
        self.check_text(text="Безопасный вход")
        self.click_any_parent_text(text="Подтвердить")
        self.check_text(text="Введите последние 6 цифр входящего номера")

    def open(self, url="/"):
        self.driver.open(f"{config.ym.url}{url}")

    def set_email(self, email: str):
        self.element('//input[@placeholder="Логин или email"]').send_keys(email)

    def set_password(self, password: str):
        self.element('//input[@placeholder="Введите пароль"]').send_keys(password)

    def set_search(self, text: str):
        self.element('//input[@placeholder="Искать на Яндекс Маркете"]').send_keys(text)
