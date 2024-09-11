import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.checkbox.checkbox_methods import CheckboxMethods
from base.pages.checkbox.checkbox_page import CheckboxPage

class CheckboxStart:
    @staticmethod
    def checkbox(page: Page, checkbox: CheckboxPage):
        errors = []
        try:
            with allure.step("Авторизация на странице Elements-> CheckboxBox"):
                AuthorizationMethod.auth_checkbox(page)

            with allure.step("Заполнение чек-боксов и их отображение"):

                with allure.step("Выбор всех чек-боксов"):
                    CheckboxMethods.click_home(checkbox)

                with allure.step("Раскрывание всех чек-боксов"):
                    CheckboxMethods.click_plus(checkbox)

                with allure.step("Скриншот результата"):
                    CheckboxMethods.screen_results(page, checkbox.screen_results)






        except AssertionError as e:
            errors.append(str(e))
