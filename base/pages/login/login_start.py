import allure
from playwright.sync_api import Page
from base.pages.buttons.buttons_page import ButtonsPage
from base.pages.buttons.buttons_methods import ButtonsMethods
from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.login.login_methods import LoginMethods
from base.pages.login.login_page import Login


class LoginStart:
    @staticmethod
    def login(page: Page, login: Login):
        errors = []
        try:
            with allure.step("Авторизация на странице Book Store Application: Login"):
                AuthorizationMethod.auth_login(page)

            with allure.step("Заполнение логина и пароля"):

                with allure.step("Заполнение логином"):
                    LoginMethods.fill_login(login)

                with allure.step("Заполнение паролем"):
                    LoginMethods.fill_password(login)

                with allure.step("Нажатие на кнопку 'Login' "):
                    LoginMethods.click_btn_login(login)

                with allure.step("Скриншот результата"):
                    ButtonsMethods.screen_results(page, filename=login.screen_results)



        except AssertionError as e:
            errors.append(str(e))