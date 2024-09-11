from playwright.sync_api import Page

from base.base import BasePage
from src.config.url import Url


class AuthorizationMethod:

    @staticmethod
    def auth_practice_form(page: Page):
        BasePage.open_page(page, Url.AUTOMATION_PRACTICE_FORM)

    @staticmethod
    def auth_textbox(page: Page):
        BasePage.open_page(page, Url.TEXT_BOX)

    @staticmethod
    def auth_checkbox(page: Page):
        BasePage.open_page(page, Url.CHECKBOX)

    @staticmethod
    def auth_radiobutton(page: Page):
        BasePage.open_page(page, Url.RADIO_BUTTON)

    @staticmethod
    def auth_buttons(page: Page):
        BasePage.open_page(page, Url.BUTTONS)

    @staticmethod
    def auth_upload_and_download(page: Page):
        BasePage.open_page(page, Url.UPLOAD_DOWNLOAD)

    @staticmethod
    def auth_modal_dialogs(page: Page):
        BasePage.open_page(page, Url.MODAL_DIALOGS)

    @staticmethod
    def auth_date_picker(page: Page):
        BasePage.open_page(page, Url.DATE_PICKER)

    @staticmethod
    def auth_select_menu(page: Page):
        BasePage.open_page(page, Url.SELECT_MENU)

    @staticmethod
    def auth_login(page: Page):
        BasePage.open_page(page, Url.LOGIN)