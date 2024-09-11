import allure
from playwright.sync_api import Page

from base.pages.date_picker.date_picker_page import Date_Picker
from base.pages.date_picker.date_picker_start import Date_Picker_Start
from conftest import date_picker


class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("Date Picker")
    @allure.title("Выбор даты")
    def test_date_picker(self, page: Page, date_picker: Date_Picker):
        Date_Picker_Start.date_picker(page, date_picker)