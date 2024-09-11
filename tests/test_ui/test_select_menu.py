import allure
from playwright.sync_api import Page

from base.pages.select_menu.select_menu_page import Select_Menu
from base.pages.select_menu.select_menu_start import Select_Menu_Start
from conftest import select_menu


class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("Select_Menu")
    @allure.title("Селекторы меню")
    def test_select_menu(self, page: Page, select_menu: Select_Menu):
        Select_Menu_Start.select_menu(page, select_menu)