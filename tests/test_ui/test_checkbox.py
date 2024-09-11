import allure
from playwright.sync_api import Page

from base.pages.checkbox.checkbox_page import CheckboxPage
from base.pages.checkbox.checkbox_start import CheckboxStart
from conftest import checkbox


class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("CheckboxBox")
    @allure.title("Заполнение чек-боксов")
    def test_checkbox(self, page: Page, checkbox: CheckboxPage):
        CheckboxStart.checkbox(page, checkbox)