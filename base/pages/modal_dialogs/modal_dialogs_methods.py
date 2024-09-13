import allure
from playwright.sync_api import Page

from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogs
from src.config.expectations import Wait

class ModalDialogs_Methods:

    @staticmethod
    def _handle_error(errors: list, e: AssertionError):
        errors.append(str(e))

    @staticmethod
    def open_small_modal(modal_dialogs: ModalDialogs):
        errors = []
        try:
            Wait.set_page(modal_dialogs.page)
            with allure.step("Нажатие на кнопку Small Modal"):
                Wait.visible(modal_dialogs.Wait_small_modal)
                modal_dialogs.small_modal.click()

        except AssertionError as e:
            ModalDialogs_Methods._handle_error(errors, e)

    @staticmethod
    def close_small_modal(modal_dialogs: ModalDialogs):
        errors = []
        try:
            Wait.set_page(modal_dialogs.page)
            with allure.step("Нажатие на кнопку 'Close' от Small Modal"):
                Wait.visible(modal_dialogs.Wait_close_small_modal)
                modal_dialogs.close_small_modal.click()

        except AssertionError as e:
            ModalDialogs_Methods._handle_error(errors, e)

    @staticmethod
    def open_large_modal(modal_dialogs: ModalDialogs):
        errors = []
        try:
            Wait.set_page(modal_dialogs.page)
            with allure.step("Нажатие на кнопку Large Modal"):
                Wait.visible(modal_dialogs.Wait_large_modal)
                modal_dialogs.large_modal.click()

        except AssertionError as e:
            ModalDialogs_Methods._handle_error(errors, e)

    @staticmethod
    def close_large_modal(modal_dialogs: ModalDialogs):
        errors = []
        try:
            Wait.set_page(modal_dialogs.page)
            with allure.step("Нажатие на кнопку 'Close' от Large Modal"):
                Wait.visible(modal_dialogs.Wait_close_large_modal)
                modal_dialogs.close_large_modal.click()

        except AssertionError as e:
            ModalDialogs_Methods._handle_error(errors, e)





    @staticmethod
    def screen_results(page: Page, filename: str):
        errors = []
        try:
            with allure.step("Скриншот результата"):
                screenshot_path = f"../../src/image/{filename}.png"
                page.screenshot(path=screenshot_path, timeout=60000)
                allure.attach.file(screenshot_path, name=filename, attachment_type=allure.attachment_type.PNG)
        except AssertionError as e:
            ModalDialogs_Methods._handle_error(errors, e)

