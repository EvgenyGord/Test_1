import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.date_picker.date_picker_methods import Date_Picker_Methods
from base.pages.date_picker.date_picker_page import Date_Picker



class Date_Picker_Start:
    @staticmethod
    def date_picker(page: Page, date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Авторизация на странице Widgets: Date Picker"):
                AuthorizationMethod.auth_date_picker(page)

            with allure.step("Селекторы выбора дат"):

                with allure.step("Открытие селектора select date"):
                    Date_Picker_Methods.click_select_date(date_picker)

                with allure.step("Открытие селектора месяца select date"):
                    Date_Picker_Methods.click_select_date_month(date_picker)

                with allure.step("Выбор месяца select date"):
                    Date_Picker_Methods.click_select_date_month_choice(date_picker)

                with allure.step("Открытие селектора года select date"):
                    Date_Picker_Methods.click_select_date_year(date_picker)

                with allure.step("Выбор года select date"):
                    Date_Picker_Methods.click_select_date_year_choice(date_picker)

                with allure.step("Выбор числа select date"):
                    Date_Picker_Methods.click_select_date_number(date_picker)

                with allure.step("Открытие селектора date and time"):
                    Date_Picker_Methods.click_date_and_time(date_picker)

                with allure.step("Открытие селектора месяца date and time"):
                    Date_Picker_Methods.click_date_and_time_month(date_picker)

                with allure.step("Выбор месяца date and time"):
                    Date_Picker_Methods.click_date_and_time_month_choice(date_picker)

                with allure.step("Открытие селектора года date and time"):
                    Date_Picker_Methods.click_date_and_time_year(date_picker)

                with allure.step("Выбор года date and time"):
                    Date_Picker_Methods.click_date_and_time_year_choice(date_picker)

                with allure.step("Выбор числа date and time"):
                    Date_Picker_Methods.click_date_and_time_number(date_picker)

                with allure.step("Выбор времени date and time"):
                    Date_Picker_Methods.click_date_and_time_hour(date_picker)

                with allure.step("Скриншот результатов"):
                    Date_Picker_Methods.screen_results(page, filename=date_picker.screen_results)



        except AssertionError as e:
            errors.append(str(e))