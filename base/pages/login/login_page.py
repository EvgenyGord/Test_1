from playwright.sync_api import Page
from base.page_factory.input import Input
from base.page_factory.button import Button

class Login:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._init_locators()
        self._init_wait_locators()
        self._init_input_data()


    def _init_locators(self):
        """Локаторы страницы: Форма"""
        self.login = Input(self.page, locator='//*[@id="userName"]', name='Ввод логина')
        self.password = Input(self.page, locator='//*[@id="password"]', name='Ввод пароля')
        self.btn_login = Button(self.page, locator='//*[@id="login"]', name='Кнопка "login"')



    def _init_wait_locators(self):
        """Локаторы ожидания"""
        self.Wait_login = '//*[@id="userName"]'
        self.Wait_btn_login = '//*[@id="login"]'
        self.Wait_password = '//*[@id="password"]'



    def _init_input_data(self):
        """Передаваемые параметры для заполнения"""
        self.screen_results = 'screen_results_login'
        self.login_text = 'evgeny_gord'
        self.password_text = '123456789Az&'
