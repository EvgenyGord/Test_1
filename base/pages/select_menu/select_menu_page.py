from playwright.sync_api import Page
from base.page_factory.button import Button

class Select_Menu:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._init_locators()
        self._init_wait_locators()
        self._init_input_data()


    def _init_locators(self):
        """Локаторы страницы: Форма"""
        self.select=self.page.locator('//*[@class=" css-1hwfws3"]')
        self.select_value_choice=Button(self.page, locator='//*[@id="react-select-2-option-0-0"]', name="Выбор значения select value")
        self.select_one_choice=Button(self.page, locator='//*[@id="react-select-3-option-0-0"]', name="Выбор значения select one")
        self.select_old=Button(self.page, locator='//*[@id="oldSelectMenu"]', name="Нажатие на селектор Old Style Select Menu")
        self.select_old_choice=self.page.locator('//*[@id="oldSelectMenu"]')
        self.select_multi_choice = Button(self.page, locator='//*[@id="react-select-4-option-1"]', name="Выбор значения 'blue' Multiselect drop down")
        self.select_cars_choice = self.page.locator('//*[@id="cars"]')
        self.select_multi_close = self.page.locator('//*[@class=" css-1wy0on6"]')





    def _init_wait_locators(self):
        """Локаторы ожидания"""
        self.Wait_select_value = '(//*[@class=" css-1hwfws3"])[1]'
        self.Wait_select_title = '(//*[@class=" css-1hwfws3"])[2]'
        self.Wait_select_xxx = '(//*[@class=" css-1hwfws3"])[3]'





    def _init_input_data(self):
        """Передаваемые параметры для заполнения"""
        self.screen_results = 'screen_results_select_menu'