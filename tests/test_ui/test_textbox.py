import allure
from playwright.sync_api import Page

from base.pages.textbox.textbox_page import TextboxPage
from base.pages.textbox.textbox_start import TextboxStart
from conftest import textbox


class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("TextBox")
    @allure.title("Заполнение текстовых полей")
    def test_textbox(self, page: Page, textbox: TextboxPage):
        TextboxStart.textbox(page, textbox)