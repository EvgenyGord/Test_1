import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.modal_dialogs.modal_dialogs_methods import ModalDialogs_Methods
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogs


class ModalDialogs_Start:
    @staticmethod
    def modal_dialogs(page: Page, modal_dialogs: ModalDialogs):
        errors = []
        try:
            with allure.step("Авторизация на странице Alerts, Frame & Windows: Modal Dialogs"):
                AuthorizationMethod.auth_modal_dialogs(page)

            with allure.step("Открытие и закрытие модальных окон"):

                with allure.step("Открытие small modal"):
                    ModalDialogs_Methods.open_small_modal(modal_dialogs)

                with allure.step("Скриншот результата small"):
                    ModalDialogs_Methods.screen_results(page, filename=modal_dialogs.screen_results_small)

                with allure.step("Закрытие small modal"):
                    ModalDialogs_Methods.close_small_modal(modal_dialogs)

                with allure.step("Открытие large modal"):
                    ModalDialogs_Methods.open_large_modal(modal_dialogs)

                with allure.step("Скриншот результата large"):
                    ModalDialogs_Methods.screen_results(page, filename=modal_dialogs.screen_results_large)

                with allure.step("Закрытие large modal"):
                    ModalDialogs_Methods.close_large_modal(modal_dialogs)






        except AssertionError as e:
            errors.append(str(e))