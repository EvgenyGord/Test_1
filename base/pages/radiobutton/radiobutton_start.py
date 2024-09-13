import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.radiobutton.radiobutton_methods import RadioButtonMethods
from base.pages.radiobutton.radiobutton_page import RadioButtonPage
from src.config.expectations import Wait


class RadioButtonStart:
    @staticmethod
    def radiobutton(page: Page, radiobutton: RadioButtonPage):
        errors = []
        try:

            with allure.step("Авторизация на странице Elements-> Radio Button"):
                AuthorizationMethod.auth_radiobutton(page)

            with allure.step("Заполнение страницы пользователем"):

                with allure.step("Нажатие на радио-кнопку Yes"):
                    RadioButtonMethods.click_radiobutton_yes(radiobutton)

                with allure.step("Скриншот результата"):
                    RadioButtonMethods.screen_results(page, radiobutton.screen_results)


        except AssertionError as e:
            errors.append(str(e))
