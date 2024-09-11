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
            with allure.step("Авторизация на странице формы"):
                AuthorizationMethod.auth_practice_form(page)

            with allure.step("Ввод данных пользователя"):
                with allure.step("Ввод имени и фамилии"):
                    PracticeFormMethods.fill_name_input(practice_form)

                with allure.step("Ввод Email"):
                    PracticeFormMethods.fill_email_input(practice_form)

                with allure.step("Выбор пола"):
                    PracticeFormMethods.fill_gender_radio_button(practice_form)

                with allure.step("Ввод номера телефона"):
                    PracticeFormMethods.fill_phone_input(practice_form)

                with allure.step("Выбор даты рождения"):
                    PracticeFormMethods.fill_date_of_birth(practice_form)

                with allure.step("Ввод и Выбор предмета"):
                    PracticeFormMethods.fill_subjects(practice_form)

                with allure.step("Выбор хобби"):
                    PracticeFormMethods.fill_hobbies(practice_form)

                with allure.step("Загрузка изображения"):
                    PracticeFormMethods.fill_load_image_picture(practice_form)

                with allure.step("Ввод Адреса"):
                    PracticeFormMethods.fill_current_address(practice_form)

                with allure.step("Выбор государства и города"):
                    PracticeFormMethods.fill_state_and_city(practice_form)

                with allure.step("Нажатие на кнопку Submit"):
                    PracticeFormMethods.button_submit(practice_form)

                with allure.step("Скриншот результата заполнения формы"):
                    PracticeFormMethods.screen_results(page, practice_form.screen_results)

        except AssertionError as e:
            errors.append(str(e))
