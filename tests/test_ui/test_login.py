import allure
from playwright.sync_api import Page

from base.pages.login.login_page import Login
from base.pages.login.login_start import LoginStart
from conftest import login


class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("Login")
    @allure.title("Логин")
    def test_login(self, page: Page, login: Login):
        LoginStart.login(page, login)
