import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.textbox.textbox_methods import TextboxMethods
from base.pages.textbox.textbox_page import TextboxPage

class TextboxStart:
    @staticmethod
    def textbox(page: Page, textbox: TextboxPage):
        errors = []
        try:
            with allure.step("Авторизация на странице Elements->TextBox"):
                AuthorizationMethod.auth_textbox(page)

            with allure.step("Ввод данных пользователя"):

                with allure.step("Ввод полного имени"):
                    TextboxMethods.fill_full_name(textbox)

                with allure.step("Ввод Email"):
                    TextboxMethods.fill_email(textbox)

                with allure.step("Ввод Current Address"):
                    TextboxMethods.fill_current_address(textbox)

                with allure.step("Ввод Permanent Address"):
                    TextboxMethods.fill_permanent_address(textbox)

                with allure.step("Нажатие на кнопку Submit"):
                    TextboxMethods.button_submit(textbox)

                with allure.step("Скриншот результата"):
                    TextboxMethods.screen_results(page, textbox.screen_results)


        except AssertionError as e:
            errors.append(str(e))
