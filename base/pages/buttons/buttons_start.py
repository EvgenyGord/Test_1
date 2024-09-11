import allure
from playwright.sync_api import Page
from base.pages.buttons.buttons_page import ButtonsPage
from base.pages.buttons.buttons_methods import ButtonsMethods
from base.pages.authorization.authorization_method import AuthorizationMethod



class ButtonsStart:
    @staticmethod
    def buttons(page: Page, buttons: ButtonsPage):
        errors = []
        try:
            with allure.step("Авторизация на странице Elements-> Buttons"):
                AuthorizationMethod.auth_buttons(page)

            with allure.step("Заполнение страницы пользователем"):

                with allure.step("Нажатие на кнопку для двойного нажатия"):
                    ButtonsMethods.button_double_click(buttons)

                with allure.step("Нажатие на кнопку для одного нажатия ПКМ"):
                    ButtonsMethods.button_right_click(buttons)

                with allure.step("Нажатие на кнопку для одного нажатия ЛКМ"):
                    ButtonsMethods.button_click(buttons)

                with allure.step("Скриншот результата"):
                    ButtonsMethods.screen_results(page, filename=buttons.screen_results)



        except AssertionError as e:
            errors.append(str(e))