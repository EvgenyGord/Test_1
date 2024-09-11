from playwright.sync_api import Page
from base.page_factory.input import Input
from base.page_factory.button import Button

class Upload_and_Download_Page:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._init_locators()
        self._init_wait_locators()
        self._init_input_data()


    def _init_locators(self):
        """Локаторы страницы: Форма"""
        self.download=Button(self.page, locator='//*[@id="downloadButton"]', name="Скачивание файла")
        self.upload=Input(self.page, locator='//*[@id="uploadFile"]', name="Загрузка файла")




    def _init_wait_locators(self):
        """Локаторы ожидания"""
        self.Wait_download = '//*[@id="downloadButton"]'
        self.Wait_upload = '//*[@id="uploadFile"]'



    def _init_input_data(self):
        """Передаваемые параметры для заполнения"""

        self.path_image = './src/image/qa_auto.jpg'  #'../../../Users/jeka2/Downloads/sampleFile.jpeg'
        self.screen_results_upload = 'screen_results_upload'