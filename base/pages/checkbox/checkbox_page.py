from playwright.sync_api import Page
from base.page_factory.button import Button

class CheckboxPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._init_locators()
        self._init_wait_locators()
        self._init_input_data()


    def _init_locators(self):
        """Локаторы страницы: Форма"""
        self.home = Button(self.page, locator='//*[@class="rct-icon rct-icon-uncheck"]', name='Чек-бокс выбора всей папки')
        self.plus = Button(self.page, locator='//*[@class="rct-icon rct-icon-expand-all"]', name='Кнопка разворачивания всей папки, просмотр всех чек-боксов')

    def _init_wait_locators(self):
        """Локаторы ожидания"""
        self.Wait_home = '//*[@class="rct-icon rct-icon-uncheck"]'
        self.Wait_plus = '//*[@class="rct-icon rct-icon-expand-all"]'

    def _init_input_data(self):
        """Передаваемые параметры для заполнения"""
        self.screen_results = 'screen_results_checkbox'
