import allure
from playwright.sync_api import Page
from base.pages.upload_and_download.upload_and_download_page import Upload_and_Download_Page
from src.config.expectations import Wait

class Upload_and_Download_Methods:

    @staticmethod
    def _handle_error(errors: list, e: AssertionError):
        errors.append(str(e))

    @staticmethod
    def download(upload_and_download: Upload_and_Download_Page):
        errors = []
        try:
            with allure.step("Скачивание файла"):
                upload_and_download.download.click()

        except AssertionError as e:
            Upload_and_Download_Methods._handle_error(errors, e)


    @staticmethod
    def upload(upload_and_download: Upload_and_Download_Page):
        errors = []
        try:
            with allure.step("Загрузка файла"):
                upload_and_download.upload.load_file(upload_and_download.path_image)
        except AssertionError as e:
            Upload_and_Download_Methods._handle_error(errors, e)



    @staticmethod
    def screen_results(page: Page, filename: str):
        errors = []
        try:
            with allure.step("Скриншот результата"):
                screenshot_path = f"../../src/image/{filename}.png"
                page.screenshot(path=screenshot_path, timeout=60000)
                allure.attach.file(screenshot_path, name=filename, attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            Upload_and_Download_Methods._handle_error(errors, e)



