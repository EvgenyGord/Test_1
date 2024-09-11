from playwright.sync_api import Page
from base.page_factory.button import Button

class RadioButtonPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._init_locators()
        self._init_wait_locators()
        self._init_input_data()


    def _init_locators(self):
        """Локаторы страницы: Форма"""
        self.button_yes = Button(self.page, locator='//*[@id="yesRadio"]/..', name='Кнопка Yes')


    def _init_wait_locators(self):
        """Локаторы ожидания"""
        self.Wait_button_yes = '//*[@id="yesRadio"]/..'


    def _init_input_data(self):
        """Передаваемые параметры для заполнения"""
        self.screen_results = 'screen_results_radiobutton'
