import time
from idlelib.iomenu import errors

import allure

from base.pages.practice_form.practice_form_page import PracticeFormPage
from src.config.expectations import Wait


class PracticeFormMethods:

    @staticmethod
    def fill_name_input(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Ввод имени и фамилии"):
                practice_form.first_name.fill(practice_form.first_name_text)
                practice_form.last_name.fill(practice_form.last_name_text)

        except AssertionError as e:
            errors.append(str(e))


    @staticmethod
    def fill_email_input(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Ввод Email"):

                practice_form.email.fill(practice_form.email_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_gender_radio_button(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Выбор пола"):
                practice_form.gender.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_phone_input(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Ввод номера телефона"):
                practice_form.phone.fill(practice_form.phone_text)
                time.sleep(4)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_date_of_birth(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Выбор даты рождения"):
                practice_form.date_of_birth.click()
                practice_form.date_of_birth_month.nth(1).click()
                practice_form.date_of_birth_month_choice.select_option(value=practice_form.month)
                practice_form.date_of_birth_year.click()
                practice_form.date_of_birth_year_choice.select_option(value=practice_form.year)
                practice_form.date_of_birth_number.click()

        except AssertionError as e:
            errors.append(str(e))


    @staticmethod
    def fill_subjects(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Ввод и Выбор предмета"):
                practice_form.subjects.fill(practice_form.subjects_text)
                practice_form.subjects_choice.click()


        except AssertionError as e:
            errors.append(str(e))


    @staticmethod
    def fill_hobbies(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Выбор хобби"):
                practice_form.hobbies_sports.click()
                practice_form.hobbies_reading.click()
                practice_form.hobbies_music.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_current_address(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Ввод Адреса"):
                practice_form.current_address.fill(practice_form.current_address_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_state_and_city(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Выбор государства и города"):
                practice_form.state.click()
                practice_form.state_choice.click()
                practice_form.city.click()
                practice_form.city_choice.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def button_submit(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Нажатие на кнопку Submit"):
                practice_form.submit_button.click()
                time.sleep(5)

        except AssertionError as e:
            errors.append(str(e))
