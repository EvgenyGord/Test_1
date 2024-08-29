import time

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
                PracticeFormMethods.fill_email_input(practice_form)
                PracticeFormMethods.fill_gender_radio_button(practice_form)
                PracticeFormMethods.fill_phone_input(practice_form)
                PracticeFormMethods.fill_date_of_birth(practice_form)
                PracticeFormMethods.fill_subjects(practice_form)
                PracticeFormMethods.fill_hobbies(practice_form)
                PracticeFormMethods.fill_current_address(practice_form)
                PracticeFormMethods.fill_state_and_city(practice_form)
                PracticeFormMethods.button_submit(practice_form)


        except AssertionError as e:
            errors.append(str(e))