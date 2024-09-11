import allure
from playwright.sync_api import Page

from base.pages.practice_form.practice_form_page import PracticeFormPage
from base.pages.practice_form.practice_start import PracticeStart
from conftest import practice_form


class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("Practice Form")
    @allure.title("Заполнение формы регистрации пользователя")
    def test_practice_form(self, page: Page, practice_form: PracticeFormPage):
        PracticeStart.practice_form(page, practice_form)
