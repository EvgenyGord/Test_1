from playwright.sync_api import Page
from base.page_factory.input import Input
from base.page_factory.button import Button

class TextboxPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._init_locators()
        self._init_wait_locators()
        self._init_input_data()


    def _init_locators(self):
        """Локаторы страницы: Форма"""
        self.full_name = Input(self.page, locator='//*[@id="userName"]', name='Full name -> Полное имя')
        self.email = Input(self.page, locator='//*[@id="userEmail"]', name='Email -> почта')
        self.current_address = Input(self.page, locator='//*[@id="currentAddress"]', name='Current Address -> Текущий адрес')
        self.permanent_address = Input(self.page, locator='//*[@id="permanentAddress"]', name='Permanent Address -> Постоянный адрес')
        self.submit_button = Button(self.page, locator='//*[@id="submit"]', name='Кнопка Submit')


    def _init_wait_locators(self):
        """Локаторы ожидания"""
        self.Wait_full_name = '//*[@id="userName"]'
        self.Wait_email = '//*[@id="userEmail"]'
        self.Wait_current_address = '//*[@id="currentAddress"]'
        self.Wait_permanent_address = '//*[@id="permanentAddress"]'
        self.Wait_button_submit = '//*[@id="submit"]'

    def _init_input_data(self):
        """Передаваемые параметры для заполнения"""
        self.full_name_text = 'Горденко Евгений Александрович'
        self.email_text = 'jeka21.02.81@mail.ru'
        self.current_address_text = 'Краснодар, ул. Текущая'
        self.permanent_address_text = 'Екатеринбург, ул. Постоянная'
        self.screen_results = 'screen_results_textbox'


