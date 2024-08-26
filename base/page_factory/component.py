from abc import ABC, abstractmethod

import allure
from playwright.sync_api import Locator, Page, expect


class Component(ABC):
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.name = name
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'компонент'

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator)

    def click(self, **kwargs) -> None:
        """
        Нажимает на элемент компонента.
        """
        with allure.step(f'Нажимаем на {self.type_of} с именем "{self.name}"'):
            self.should_be_visible()
            locator = self.get_locator(**kwargs)
            locator.click()

    def focus(self, **kwargs) -> None:
        """
        Устанавливает фокус на элемент компонента.
        """
        with allure.step(f'Фокус на {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.focus()

    def should_be_visible(self, **kwargs) -> None:
        """
        Проверяет видимость элемента компонента.
        """
        with allure.step(f'Проверка видимости {self.type_of} "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.wait_for(state="visible")
            expect(locator).to_be_visible()

    def should_be_hidden(self, timeout: int = 5, **kwargs) -> None:
        """
        Проверяет скрытость элемента компонента.
        """
        with allure.step(f'Проверка скрытости {self.type_of} "{self.name}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_hidden(timeout=timeout * 1000)

    def should_have_text(self, text: str, **kwargs) -> None:
        """
        Проверяет текст элемента компонента на наличие определенного значения.
        """
        with allure.step(f'Проверка текста {self.type_of} "{self.name}" на наличие "{text}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_text(text)

    def should_not_be_disabled(self, **kwargs) -> None:
        """
        Проверяет, что элемент компонента не заблокирован.
        """
        with allure.step(f'Проверка активности {self.type_of} "{self.name}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).not_to_be_disabled()

    def should_be_disabled(self, **kwargs) -> None:
        """
        Проверяет, что элемент компонента заблокирован.
        """
        with allure.step(f'Проверка неактивности {self.type_of} "{self.name}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_disabled()