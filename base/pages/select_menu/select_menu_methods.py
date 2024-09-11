import allure
from playwright.sync_api import Page
from base.pages.select_menu.select_menu_page import Select_Menu

from src.config.expectations import Wait

class Select_Menu_Methods:

    @staticmethod
    def _handle_error(errors: list, e: AssertionError):
        errors.append(str(e))

    @staticmethod
    def click_select_value(select_menu: Select_Menu):
        errors = []
        try:
            with allure.step("Нажатие на селектор Select Value"):
                select_menu.select.nth(0).click()

        except AssertionError as e:
            Select_Menu_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_one(select_menu: Select_Menu):
        errors = []
        try:
            with allure.step("Нажатие на селектор Select One"):
                select_menu.select.nth(1).click()

        except AssertionError as e:
            Select_Menu_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_xxx(select_menu: Select_Menu):
        errors = []
        try:
            with allure.step("Нажатие на селектор Multiselect drop down"):
                select_menu.select.nth(2).click()

        except AssertionError as e:
            Select_Menu_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_old(select_menu: Select_Menu):
        errors = []
        try:
            with allure.step("Нажатие на селектор Old Style Select Menu"):
                select_menu.select_old.click()

        except AssertionError as e:
            Select_Menu_Methods._handle_error(errors, e)


    @staticmethod
    def click_select_value_choice(select_menu: Select_Menu):
        errors = []
        try:
            with allure.step("Выбор значения селектор Select Value"):
                select_menu.select_value_choice.click()

        except AssertionError as e:
            Select_Menu_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_one_choice(select_menu: Select_Menu):
        errors = []
        try:
            with allure.step("Выбор значения селектор Select One"):
                select_menu.select_one_choice.click()

        except AssertionError as e:
            Select_Menu_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_old_choice(select_menu: Select_Menu):
        errors = []
        try:
            with allure.step("Выбор значения селектор Old Style Select Menu"):
                select_menu.select_old_choice.click()

        except AssertionError as e:
            Select_Menu_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_multi_choice(select_menu: Select_Menu):
        errors = []
        try:
            with allure.step("Выбор значения селектор Multiselect drop down"):
                select_menu.select_multi_choice.click()
                select_menu.select_multi_close.nth(2).click()


        except AssertionError as e:
            Select_Menu_Methods._handle_error(errors, e)

    @staticmethod
    def click_select_cars_choice(select_menu: Select_Menu):
        errors = []
        try:
            with allure.step("Выбор значения селектор Standard multi select"):
                select_menu.select_cars_choice.click()


        except AssertionError as e:
            Select_Menu_Methods._handle_error(errors, e)





    @staticmethod
    def screen_results(page: Page, filename: str):
        errors = []
        try:
            with allure.step("Скриншот результата"):
                screenshot_path = f"../../src/image/{filename}.png"
                page.screenshot(path=screenshot_path, timeout=60000)
                allure.attach.file(screenshot_path, name=filename, attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            Select_Menu_Methods._handle_error(errors, e)