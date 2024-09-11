import allure
from playwright.sync_api import Page

from base.pages.radiobutton.radiobutton_page import RadioButtonPage
from base.pages.radiobutton.radiobutton_start import RadioButtonStart
from conftest import radiobutton


class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("RadioButton")
    @allure.title("Выбор и нажатие на кнопку")
    def test_radiobutton(self, page: Page, radiobutton: RadioButtonPage):
        RadioButtonStart.radiobutton(page, radiobutton)