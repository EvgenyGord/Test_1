import allure
from playwright.sync_api import Page

from base.pages.buttons.buttons_page import ButtonsPage
from base.pages.buttons.buttons_start import ButtonsStart
from conftest import buttons


class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("Buttons")
    @allure.title("Выбор и нажатие на кнопку")
    def test_buttons(self, page: Page, buttons: ButtonsPage):
        ButtonsStart.buttons(page, buttons)
