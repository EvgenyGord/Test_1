import allure
from playwright.sync_api import Page
from base.pages.textbox.textbox_page import TextboxPage
from src.config.expectations import Wait

class TextboxMethods:

    @staticmethod
    def _handle_error(errors: list, e: AssertionError):
        errors.append(str(e))

    @staticmethod
    def fill_full_name(textbox: TextboxPage):
        errors = []
        try:
            with allure.step("Заполнение полного имени"):
                textbox.full_name.fill(textbox.full_name_text)

        except AssertionError as e:
            TextboxMethods._handle_error(errors, e)

    @staticmethod
    def fill_email(textbox: TextboxPage):
        errors = []
        try:
            with allure.step("Заполнение почты -> Email"):
                textbox.email.fill(textbox.email_text)

        except AssertionError as e:
            TextboxMethods._handle_error(errors, e)

    @staticmethod
    def fill_current_address(textbox: TextboxPage):
        errors = []
        try:
            with allure.step("Заполнение текущего адреса -> Сurrent Address"):
                textbox.current_address.fill(textbox.current_address_text)

        except AssertionError as e:
            TextboxMethods._handle_error(errors, e)

    @staticmethod
    def fill_permanent_address(textbox: TextboxPage):
        errors = []
        try:
            with allure.step("Заполнение постоянного адреса -> Permanent Address"):
                textbox.permanent_address.fill(textbox.permanent_address_text)

        except AssertionError as e:
            TextboxMethods._handle_error(errors, e)

    @staticmethod
    def button_submit(textbox: TextboxPage):
        errors = []
        Wait.set_page(textbox.page)
        try:
            with allure.step("Нажатие на кнопку отправки формы"):
                textbox.submit_button.click()
                Wait.visible(textbox.Wait_button_submit)
        except AssertionError as e:
            TextboxMethods._handle_error(errors, e)

    @staticmethod
    def screen_results(page: Page, filename: str):
        errors = []
        try:
            with allure.step("Скриншот результата"):
                screenshot_path = f"../../src/image/{filename}.png"
                page.screenshot(path=screenshot_path, timeout=60000)
                allure.attach.file(screenshot_path, name=filename, attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            TextboxMethods._handle_error(errors, e)