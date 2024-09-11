from playwright.sync_api import Page
from base.page_factory.button import Button

class ButtonsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._init_locators()
        self._init_wait_locators()
        self._init_input_data()


    def _init_locators(self):
        """Локаторы страницы: Форма"""
        self.button_double_click = Button(self.page, locator='//*[@id="doubleClickBtn"]', name='Кнопка для двойного нажатия ЛКМ')
        self.button_right_click = Button(self.page, locator='//*[@id="rightClickBtn"]', name='Кнопка для нажатия ПКМ')
        self.button_click = self.page.locator('//*[contains(text(), "Click Me")]')



    def _init_wait_locators(self):
        """Локаторы ожидания"""
        self.Wait_button_double_click = '//*[@id="doubleClickBtn"]'
        self.Wait_button_right_click = '//*[@id="rightClickBtn"]'
        self.Wait_button_click = '(//*[contains(text(), "Click Me")])[3]'


    def _init_input_data(self):
        """Передаваемые параметры для заполнения"""
        self.screen_results = 'screen_results_buttons'