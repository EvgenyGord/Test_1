import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.select_menu.select_menu_methods import Select_Menu_Methods
from base.pages.select_menu.select_menu_page import Select_Menu


class Select_Menu_Start:
    @staticmethod
    def select_menu(page: Page, select_menu: Select_Menu):
        errors = []
        try:
            with allure.step("Авторизация на странице Widgets: Select Menu"):
                AuthorizationMethod.auth_select_menu(page)

            with allure.step("Селекторы прохождение"):

                with allure.step("Открытие селектора select value"):
                    Select_Menu_Methods.click_select_value(select_menu)

                with allure.step("Выбор значения в select value"):
                    Select_Menu_Methods.click_select_value_choice(select_menu)

                with allure.step("Открытие селектора Select One"):
                    Select_Menu_Methods.click_select_one(select_menu)

                with allure.step("Выбор значения в Select One"):
                    Select_Menu_Methods.click_select_one_choice(select_menu)

                with allure.step("Открытие селектора Old Style Select Menu"):
                    Select_Menu_Methods.click_select_old(select_menu)

                with allure.step("Выбор значения в Old Style Select Menu"):
                    Select_Menu_Methods.click_select_old_choice(select_menu)

                with allure.step("Открытие селектора Multiselect drop down"):
                    Select_Menu_Methods.click_select_xxx(select_menu)

                with allure.step("Выбор значения в Multiselect drop down"):
                    Select_Menu_Methods.click_select_multi_choice(select_menu)

                with allure.step("Выбор значения в Standard multi select"):
                    Select_Menu_Methods.click_select_cars_choice(select_menu)

                with allure.step("Скриншот результата"):
                    Select_Menu_Methods.screen_results(page, filename=select_menu.screen_results)




        except AssertionError as e:
            errors.append(str(e))