import allure
from playwright.sync_api import Page
from base.pages.buttons.buttons_page import ButtonsPage
from base.pages.login.login_page import Login
from src.config.expectations import Wait

class LoginMethods:

    @staticmethod
    def _handle_error(errors: list, e: AssertionError):
        errors.append(str(e))

    @staticmethod
    def fill_login(login: Login):
        errors = []
        try:
            with allure.step("Ввод логина"):
                login.login.fill(login.login_text)

        except AssertionError as e:
            LoginMethods._handle_error(errors, e)

    @staticmethod
    def fill_password(login: Login):
        errors = []
        try:
            with allure.step("Ввод пароля"):
                login.password.fill(login.password_text)

        except AssertionError as e:
            LoginMethods._handle_error(errors, e)

    @staticmethod
    def click_btn_login(login: Login):
        errors = []
        try:
            with allure.step("Нажатие на кнопку 'Login'"):
                login.btn_login.click()

        except AssertionError as e:
            LoginMethods._handle_error(errors, e)




    @staticmethod
    def screen_results(page: Page, filename: str):
        errors = []
        try:
            with allure.step("Скриншот результата"):
                screenshot_path = f"../../src/image/{filename}.png"
                page.screenshot(path=screenshot_path, timeout=60000)
                allure.attach.file(screenshot_path, name=filename, attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            LoginMethods._handle_error(errors, e)