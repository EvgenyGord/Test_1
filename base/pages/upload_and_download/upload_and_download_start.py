import allure
from playwright.sync_api import Page
from base.pages.upload_and_download.upload_and_download_methods import Upload_and_Download_Methods
from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.upload_and_download.upload_and_download_page import Upload_and_Download_Page
from conftest import upload_and_download


class Upload_and_Download_Start:
    @staticmethod
    def upload_and_download(page: Page, upload_and_download: Upload_and_Download_Page):
        errors = []
        try:
            with allure.step("Авторизация на странице Elements-> Upload and Download"):
                AuthorizationMethod.auth_upload_and_download(page)

            with allure.step("Заагрузка и скачивание файлов"):

                with allure.step("Скачивание файла"):
                    Upload_and_Download_Methods.download(upload_and_download)


                with allure.step("Загрузка файла"):
                    Upload_and_Download_Methods.upload(upload_and_download)

                with allure.step("Скриншот результата"):
                    Upload_and_Download_Methods.screen_results(page, filename=upload_and_download.screen_results_upload)



        except AssertionError as e:
            errors.append(str(e))