import allure
from playwright.sync_api import Page

from base.pages.date_picker.date_picker_page import Date_Picker
from src.config.expectations import Wait

class Date_Picker_Methods:

    @staticmethod
    def _handle_error(errors: list, e: AssertionError):
        errors.append(str(e))

    @staticmethod
    def click_select_date(date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Нажатие на селектор select date"):
                date_picker.select_date.click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_date_month(date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Нажатие на селектор месяца select date"):
                date_picker.select_date_month.click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_date_month_choice(date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Выбор месяца select date"):
                date_picker.select_date_month_choice.select_option(value="10")
        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_date_year(date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Нажатие на селектор года select date"):
                date_picker.select_date_year.click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_date_year_choice(date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Выбор года select date"):
                date_picker.select_date_year_choice.select_option(value="2022")

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_date_number(date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Выбор числа select date"):
                date_picker.select_date_number_choice.click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_date_and_time(date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Нажатие на селектор date_and_time"):
                date_picker.date_and_time.click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_date_and_time_month(date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Нажатие на селектор месяца date_and_time"):
                date_picker.date_and_time_month.click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_date_and_time_month_choice(date_picker: Date_Picker):
        errors = []
        try:
            Wait.set_page(date_picker.page)
            with allure.step("Выбор месяца date_and_time"):
                Wait.visible(date_picker.Wait_date_and_time_month_choice)
                date_picker.date_and_time_month_choice.nth(9).click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_date_and_time_year(date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Нажатие на селектор года date_and_time"):
                date_picker.date_and_time_year.click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_date_and_time_year_choice(date_picker: Date_Picker):
        errors = []
        try:
            Wait.set_page(date_picker.page)
            with allure.step("Выбор года date_and_time"):
                Wait.visible(date_picker.Wait_date_and_time_year_choice)
                date_picker.date_and_time_year_choice.nth(9).click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_date_and_time_number(date_picker: Date_Picker):
        errors = []
        try:
            with allure.step("Выбор числа date_and_time"):
                date_picker.date_and_time_number_choice.click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)

    @staticmethod
    def click_date_and_time_hour(date_picker: Date_Picker):
        errors = []
        try:
            Wait.set_page(date_picker.page)
            with allure.step("Выбор времени date_and_time"):
                Wait.set_page(date_picker.Wait_date_and_time_number_choice)
                date_picker.date_and_time_hour_choice.nth(0).click()

        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)


    @staticmethod
    def screen_results(page: Page, filename: str):
        errors = []
        try:
            with allure.step("Скриншот результата"):
                screenshot_path = f"../../src/image/{filename}.png"
                page.screenshot(path=screenshot_path, timeout=60000)
                allure.attach.file(screenshot_path, name=filename, attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            Date_Picker_Methods._handle_error(errors, e)