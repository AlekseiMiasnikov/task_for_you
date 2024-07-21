import pytest

from pages.yandex_market.yandex_market_basket_page import YandexMarketBasketPage
from pages.yandex_market.yandex_market_page import YandexMarketPage


@pytest.fixture(scope="function")
def yandex_market_page(browser):
    return YandexMarketPage(browser=browser)


@pytest.fixture(scope="function")
def yandex_market_basket_page(browser):
    return YandexMarketBasketPage(browser=browser)
