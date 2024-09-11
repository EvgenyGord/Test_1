import allure
from playwright.sync_api import Page
from base.pages.checkbox.checkbox_page import CheckboxPage
from src.config.expectations import Wait

class CheckboxMethods:

    @staticmethod
    def _handle_error(errors: list, e: AssertionError):
        errors.append(str(e))

    @staticmethod
    def click_home(checkbox: CheckboxPage):
        errors = []
        try:
            with allure.step("Нажатие на чек-бокс всей папки Home"):
                checkbox.home.click()


        except AssertionError as e:
            CheckboxMethods._handle_error(errors, e)

    @staticmethod
    def click_plus(checkbox: CheckboxPage):
        errors = []
        try:
            with allure.step("Нажатие на +, разворачивание всех чек-боксов"):
                checkbox.plus.click()

        except AssertionError as e:
            CheckboxMethods._handle_error(errors, e)


    @staticmethod
    def screen_results(page: Page, filename: str):
        errors = []
        try:
            with allure.step("Скриншот результата"):
                screenshot_path = f"../../src/image/{filename}.png"
                page.screenshot(path=screenshot_path, timeout=60000)
                allure.attach.file(screenshot_path, name=filename, attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            CheckboxMethods._handle_error(errors, e)
