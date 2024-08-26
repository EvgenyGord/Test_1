from playwright.sync_api import Page


class Expectations:
    DEFAULT_TIMEOUT = 5 * 1000


class Wait:
    W1s = 1000
    W2s = 2000
    W3s = 3000
    W4s = 4000
    W5s = 5000
    W6s = 6000
    W7s = 7000
    W8s = 8000
    W9s = 9000
    W10s = 10000
    W11s = 11000
    W12s = 12000
    W13s = 13000
    W14s = 14000
    W15s = 15000

    _page = None

    @staticmethod
    def set_page(page):
        Wait._page = page

    @staticmethod
    def visible(locator, timeout=W10s):
        try:
            Wait._page.wait_for_selector(locator, state="visible", timeout=timeout)
        except TimeoutError:
            print(f"Ожидание {timeout / 1000} секунд не завершено, элемент не виден.")

    @staticmethod
    def load_state(page: Page, timeout=W10s):
        try:
            page.wait_for_load_state(state="load", timeout=timeout)
        except TimeoutError:
            print(f"Ожидание загрузки страницы {timeout} секунд не завершено.")