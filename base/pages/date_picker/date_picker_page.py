from playwright.sync_api import Page
from base.page_factory.button import Button

class Date_Picker:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._init_locators()
        self._init_wait_locators()
        self._init_input_data()


    def _init_locators(self):
        """Локаторы страницы: Форма"""
        self.select_date=Button(self.page, locator='//*[@id="datePickerMonthYearInput"]', name="Нажатие на селектор select date")
        self.select_date_month = Button(self.page, locator='//*[@class="react-datepicker__month-select"]', name = "Нажатие на селектор месяца select date")
        self.select_date_month_choice = self.page.locator('//*[@class="react-datepicker__month-select"]')
        self.select_date_year = Button(self.page, locator='//*[@class="react-datepicker__year-select"]', name="Нажатие на селектор года select date")
        self.select_date_year_choice = self.page.locator('//*[@class="react-datepicker__year-select"]')
        self.select_date_number_choice = Button(self.page, locator='//*[@class="react-datepicker__day react-datepicker__day--024"]', name = "Выбор числа select date")
        self.date_and_time = Button(self.page, locator='//*[@id="dateAndTimePickerInput"]', name="Нажатие на селектор date and time")
        self.date_and_time_month = Button(self.page, locator='//*[@class="react-datepicker__month-read-view--selected-month"]', name="Нажатие на селектор месяца date and time")
        self.date_and_time_month_choice = self.page.locator('//*[@class="react-datepicker__month-option"]')
        self.date_and_time_year = Button(self.page, locator='//*[@class="react-datepicker__year-read-view--selected-year"]', name="Нажатие на селектор года date and time")
        self.date_and_time_year_choice = self.page.locator('//*[@class="react-datepicker__year-option"]')
        self.date_and_time_number_choice = Button(self.page, locator='//*[@class="react-datepicker__day react-datepicker__day--024"]', name="Выбор числа date and time")
        self.date_and_time_hour_choice = self.page.locator('//*[@class="react-datepicker__time-list"]/li')


    def _init_wait_locators(self):
        """Локаторы ожидания"""
        self.Wait_date_and_time_month_choice = '(//*[@class="react-datepicker__month-option"])[10]'
        self.Wait_date_and_time_year_choice = '(//*[@class="react-datepicker__year-option"])[10]'
        self.Wait_date_and_time_number_choice = '(//*[@class="react-datepicker__time-list"]/li)[1]'




    def _init_input_data(self):
        """Передаваемые параметры для заполнения"""
        self.screen_results = 'screen_results_date_picker'
