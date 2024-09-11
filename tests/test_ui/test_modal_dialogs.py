import allure
from playwright.sync_api import Page

from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogs
from base.pages.modal_dialogs.modal_dialogs_start import ModalDialogs_Start
from conftest import modal_dialogs


class TestPractice:

    @allure.epic("Тесты потока 1")
    @allure.feature("Modal Dialogs")
    @allure.title("Модальные окна")
    def test_modal_dialogs(self, page: Page, modal_dialogs: ModalDialogs):
        ModalDialogs_Start.modal_dialogs(page, modal_dialogs)



