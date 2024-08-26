import os
import platform
import allure
from playwright.sync_api import Page, TimeoutError


class BasePage:

    def __init__(self, page: Page, context=None) -> None:
        self.page = page
        self.context = context

    @staticmethod
    def open_page(page: Page, url: str) -> None:
        try:
            page.goto(url, timeout=5000, wait_until='domcontentloaded')
        except TimeoutError:
            print("Тест дождался пока страница загрузится, продолжился и выполнился")

    class Base:
        def __init__(self, browser, url):
            self.browser = browser
            self.url = url
            self.timeout = 15

            if "Linux" in platform.platform():
                self.DIR_PATH = "/".join(os.getcwd().split("/")[:-2])

        def send_file(self, locator, path):
            element = self.wait_for_element(locator)
            element.set_input_files(path)

        def simple_click(self, locator):
            element = self.wait_for_element(locator)
            element.click()

        def click(self, locator):
            element = self.wait_for_element(locator)
            element.scroll_into_viewIfNeeded()
            element.click()

        def press_enter(self):
            print('Нажимаю на "ENTER"')
            self.browser.keyboard.press("Enter")

        def scroll_to(self, locator):
            element = self.wait_for_element(locator)
            element.scroll_into_viewIfNeeded()

        def scroll_to_element(self, locator, timeout=5):
            element = self.wait_for_element(locator, timeout)
            element.scroll_into_viewIfNeeded()

        def clear_text(self, locator):
            element = self.wait_for_element(locator)
            element.fill("")

        def get_element_text(self, locator):
            element = self.wait_for_element(locator)
            return element.text_content()

        def get_attr(self, locator, value):
            element = self.wait_for_element(locator)
            return element.get_attribute(value)

        def screen(self, filename, name):
            screenshot_path = f"screenshots/{filename}.png"
            self.browser.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)

        def wait_for_element(self, locator, timeout=None):
            return self.browser.wait_for_selector(locator, timeout=timeout)