from playwright.sync_api import Page
from base.page_factory.button import Button

class ModalDialogs:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._init_locators()
        self._init_wait_locators()
        self._init_input_data()


    def _init_locators(self):
        """Локаторы страницы: Форма"""
        self.small_modal=Button(self.page, locator='//*[@id="showSmallModal"]', name="Кнопка открытия small modal")
        self.close_small_modal=Button(self.page, locator='//*[@id="closeSmallModal"]', name="Кнопка закрытия small modal")
        self.large_modal=Button(self.page, locator='//*[@id="showLargeModal"]', name="Кнопка открытия large modal")
        self.close_large_modal=Button(self.page, locator='//*[@id="closeLargeModal"]', name="Кнопка закрытия large modal")





    def _init_wait_locators(self):
        """Локаторы ожидания"""
        self.Wait_small_modal = '//*[@id="showSmallModal"]'
        self.Wait_close_small_modal = '//*[@id="closeSmallModal"]'
        self.Wait_large_modal = '//*[@id="showLargeModal"]'
        self.Wait_close_large_modal = '//*[@id="closeLargeModal"]'



    def _init_input_data(self):
        """Передаваемые параметры для заполнения"""


        self.screen_results_small = 'screen_results_small_modal'
        self.screen_results_large = 'screen_results_large_modal'