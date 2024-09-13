import allure
from playwright.sync_api import Page
from base.pages.radiobutton.radiobutton_page import RadioButtonPage
from src.config.expectations import Wait

class RadioButtonMethods:

    @staticmethod
    def _handle_error(errors: list, e: AssertionError):
        errors.append(str(e))

    @staticmethod
    def click_radiobutton_yes(radiobutton: RadioButtonPage):
        errors = []
        try:
            Wait.set_page(radiobutton.page)
            with allure.step("Нажатие на кнопку Yes"):
                Wait.visible(radiobutton.Wait_button_yes)
                radiobutton.button_yes.click()

        except AssertionError as e:
            RadioButtonMethods._handle_error(errors, e)



    @staticmethod
    def screen_results(page: Page, filename: str):
        errors = []
        try:
            with allure.step("Скриншот результата"):
                screenshot_path = f"../../src/image/{filename}.png"
                page.screenshot(path=screenshot_path, timeout=60000)
                allure.attach.file(screenshot_path, name=filename, attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            RadioButtonMethods._handle_error(errors, e)
