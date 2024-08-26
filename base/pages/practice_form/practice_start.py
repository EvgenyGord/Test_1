import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.practice_form.practice_form_methods import PracticeFormMethods
from base.pages.practice_form.practice_form_page import PracticeFormPage


class PracticeStart:
    @staticmethod
    def practice_form(page: Page, practice_form: PracticeFormPage):
        errors = []
        try:
            AuthorizationMethod.auth_practice_form(page)

            with allure.step("Ввод данных пользователя"):
                PracticeFormMethods.fill_name_input(practice_form)

        except AssertionError as e:
            errors.append(str(e))