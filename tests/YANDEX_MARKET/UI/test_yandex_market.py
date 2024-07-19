from pytest import mark
from pages.yandex_market.yandex_market_page import YandexMarketPage


@mark.yandex_market
class TestYandexMarket:
    def test_yandex_market_add_item(self, yandex_market_page: YandexMarketPage):

        # auth
        yandex_market_page.auth_yandex_market()

        # autotest
        yandex_market_page.set_search(text="Ноутбуки HP")
        yandex_market_page.click_any_parent_text(text="Найти")
        yandex_market_page.click_any_text(text="подешевле", js_click=True)
        yandex_market_page.click_any_text(text="8 ГБ", js_click=True)
        yandex_market_page.click_any_contains_parent_text(text="корзину")
        yandex_market_page.check_text(text="Товар успешно добавлен в корзину")
        yandex_market_page.click_any_text(text="Перейти в корзину")
        yandex_market_page.check_text(text=["Корзина", "Перейти к оформлению"])
        yandex_market_page.save_screenshot(filename="your_filename")

        # delete items
        yandex_market_page.click_any_parent_text(text="Удалить выбранные")
        yandex_market_page.check_text(text="Сложите в корзину нужные товары")
        yandex_market_page.click_any_parent_text(text="Удалить")