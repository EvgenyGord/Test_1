from playwright.sync_api import Page
from base.page_factory.button import Button
from base.page_factory.input import Input


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._init_locators()
        self._init_wait_locators()
        self._init_input_data()

    def _init_locators(self):
        """Локаторы страницы: Форма"""
        self.first_name = Input(self.page, locator='//*[@id="firstName"]', name='Имя')
        self.last_name = Input(self.page, locator='//*[@id="lastName"]', name='Фамилия')
        self.email = Input(self.page, locator='//*[@id="userEmail"]', name='Email')
        self.gender = Button(self.page, locator='//*[@for="gender-radio-1"]', name='Пол')
        self.phone = Input(self.page, locator='//*[@id="userNumber"]', name='Телефон')
        self.date_of_birth = Button(self.page, locator='//*[@id="dateOfBirthInput"]', name='Дата рождения')
        self.date_of_birth_month = self.page.locator('//*[starts-with(@class, "react-datepicker__month")]')
        self.date_of_birth_month_choice = self.page.locator('//select//*[@value="10"]/..')
        self.date_of_birth_year = Button(self.page, locator='//select[contains(@class, "year")]', name='Выпадающий список годов')
        self.date_of_birth_year_choice = self.page.locator('//select//*[@value="2002"]/..')
        self.date_of_birth_number = Button(self.page, locator='.react-datepicker__day--024', name='Выбор числа')
        self.subjects = Input(self.page, locator='//*[@id="subjectsInput"]', name='Предмет')
        self.subjects_choice = Button(self.page, locator='//*[@id="react-select-2-option-0"]', name='Выбор предмета')
        self.hobbies_sports = Button(self.page, locator='//*[@id="hobbies-checkbox-1"]/..', name='Выбор хобби -> спорт')
        self.hobbies_reading = Button(self.page, locator='//*[@id="hobbies-checkbox-2"]/..', name='Выбор хобби -> чтение')
        self.hobbies_music = Button(self.page, locator='//*[@id="hobbies-checkbox-3"]/..', name='Выбор хобби -> музыка')
        self.current_address = Input(self.page, locator='//*[@id="currentAddress"]', name='Адрес')
        self.load_files_pictures = Input(self.page, locator='//*[@id="uploadPicture"]', name='Загрузка файлов изображений')
        self.state = Button(self.page, locator='//*[@id="stateCity-wrapper"]//div[contains(text(), "Select State")]', name='Государство')
        self.state_choice = Button(self.page, locator='//*[@id="react-select-3-option-0"]', name='Выбор государства')
        self.city = Button(self.page, locator='//*[@id="stateCity-wrapper"]//div[contains(text(), "Select City")]', name='Город')
        self.city_choice = Button(self.page, locator='//*[@id="react-select-4-option-0"]', name='Выбор города')
        self.submit_button = Button(self.page, locator='//*[@id="submit"]', name='Кнопка Submit')



    def _init_wait_locators(self):
        """Локаторы ожидания"""
        self.Wait_first_name = '//*[@id="firstName"]'
        self.Wait_last_name = '//*[@id="lastName"]'
        self.Wait_email = '//*[@id="userEmail"]'
        self.Wait_gender = '//*[@for="gender-radio-1"]'
        self.Wait_telephone = '//*[@id="userNumber"]'
        self.Wait_date_of_birth = '//*[@id="dateOfBirthInput"]'
        self.Wait_date_of_birth_month = '(//*[starts-with(@class, "react-datepicker__month")])[2]'
        self.Wait_date_of_birth_month_choice = '//select//*[@value="10"]/..'
        self.Wait_date_of_birth_year = '//select[contains(@class, "year")]'
        self.Wait_date_of_birth_year_choice = '//select//*[@value="2002"]/..'
        self.Wait_subjects = '//*[@id="subjectsInput"]'
        self.Wait_subjects_choice = '//*[@id="react-select-2-option-0"]'
        self.Wait_hobbies_sports = '//*[@id="hobbies-checkbox-1"]'
        self.Wait_hobbies_reading = '//*[@id="hobbies-checkbox-2"]'
        self.Wait_hobbies_music = '//*[@id="hobbies-checkbox-3"]'
        self.Wait_load_files_pictures = '//*[@id="uploadPicture"]'
        self.Wait_current_address = '//*[@id="currentAddress"]'
        self.Wait_state = '//*[@id="stateCity-wrapper"]//div[contains(text(), "Select State")]'
        self.Wait_state_choice = '//*[@id="react-select-3-option-0"]'
        self.Wait_city = '//*[@id="stateCity-wrapper"]//div[contains(text(), "Select City")]'
        self.Wait_city_choice = '//*[@id="react-select-4-option-0"]'
        self.Wait_button_submit = '//*[@id="submit"]'

    def _init_input_data(self):
        """Передаваемые параметры для заполнения"""
        self.first_name_text = 'Евгений'
        self.last_name_text = 'Горденко'
        self.email_text = 'jeka21.02.81@mail.ru'
        self.phone_text = '9531187947'
        self.month = '10'
        self.year = '2002'
        self.subjects_text = 'English'
        self.current_address_text = 'Krasnodar'
        self.path_image = './src/image/qa_auto.jpg'
        self.screen_results = 'screen_results_practice_form'

