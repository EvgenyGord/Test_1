import allure
from playwright.sync_api import Page
from base.pages.buttons.buttons_page import ButtonsPage
from src.config.expectations import Wait

class ButtonsMethods:

    @staticmethod
    def _handle_error(errors: list, e: AssertionError):
        errors.append(str(e))

    @staticmethod
    def button_double_click(buttons: ButtonsPage):
        errors = []
        try:
            Wait.set_page(buttons.page)
            with allure.step("Нажатие на кнопку для двойного нажатия ЛКМ"):
                Wait.visible(buttons.Wait_button_double_click)
                buttons.button_double_click.double_click()

        except AssertionError as e:
            ButtonsMethods._handle_error(errors, e)

    @staticmethod
    def button_right_click(buttons: ButtonsPage):
        errors = []
        try:
            Wait.set_page(buttons.page)
            with allure.step("Нажатие на кнопку для нажатия ПКМ"):
                Wait.visible(buttons.Wait_button_right_click)
                buttons.button_right_click.click_right()

        except AssertionError as e:
            ButtonsMethods._handle_error(errors, e)

    @staticmethod
    def button_click(buttons: ButtonsPage):
        errors = []
        try:
            Wait.set_page(buttons.page)
            with allure.step("Нажатие на кнопку для одного нажатия ЛКМ"):
                Wait.visible(buttons.Wait_button_click)
                buttons.button_click.nth(2).click()

        except AssertionError as e:
            ButtonsMethods._handle_error(errors, e)



    @staticmethod
    def screen_results(page: Page, filename: str):
        errors = []
        try:
            with allure.step("Скриншот результата"):
                screenshot_path = f"../../src/image/{filename}.png"
                page.screenshot(path=screenshot_path, timeout=60000)
                allure.attach.file(screenshot_path, name=filename, attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            ButtonsMethods._handle_error(errors, e)