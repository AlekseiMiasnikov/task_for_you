from dotenv import load_dotenv
from pydantic import Extra
from pydantic_settings import BaseSettings

load_dotenv()


class YandexMarket(BaseSettings):
    class Config:
        extra = Extra.allow
        env_file = ".env"
        env_prefix = "YANDEX_MARKET_"
        env_file_encoding = "utf-8"

    url: str = "https://market.yandex.ru/"
    username: str
    password: str


class Config(BaseSettings):
    """Настройки для тестов."""

    class Config:
        extra = Extra.allow
        env_file = ".env"
        env_prefix = "BASE_"
        env_file_encoding = "utf-8"

    browser_name: str = "chrome"
    browser_window_width: str = "1920"
    browser_window_height: str = "1080"
    timeout: int = 60
    ym: YandexMarket = YandexMarket()


config = Config()
