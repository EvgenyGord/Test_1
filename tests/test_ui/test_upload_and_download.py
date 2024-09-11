import allure
from playwright.sync_api import Page

from base.pages.upload_and_download.upload_and_download_page import Upload_and_Download_Page
from base.pages.upload_and_download.upload_and_download_start import Upload_and_Download_Start
from conftest import upload_and_download


class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("Upload and Download")
    @allure.title("Отправка и загрузка")
    def test_checkbox(self, page: Page, upload_and_download: Upload_and_Download_Page):
        Upload_and_Download_Start.upload_and_download(page, upload_and_download)