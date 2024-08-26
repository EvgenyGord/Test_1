import time

import allure

from base.page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return 'кнопка'

    def hover(self, **kwargs) -> None:
        """
        Выполняет наведение курсора на кнопку.
        """
        with allure.step(f'Наведение курсора на {self.type_of} с именем "{self.name}"'):
            self.should_be_visible()
            locator = self.get_locator(**kwargs)
            locator.hover()

    def double_click(self, **kwargs):
        """
        Двойное нажатие на кнопку.
        """
        with allure.step(f'Двойное нажатие на {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.dblclick()

    def on_click(self, **kwargs) -> None:
        """
        Нажатие на кнопку.
        """
        with allure.step(f'Нажатие на {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.click()

    def check_class(self, name, **kwargs):
        """
        Проверка класса кнопки.
        """
        with allure.step(f'Проверка класса {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            time.sleep(2)
            classes = locator.get_attribute("class")
            ass = name in classes
            assert ass, f"{self.name} -> {ass}"

    def is_visible(self, last=False, **kwargs):
        """
        Проверка видимости кнопки.
        """
        with allure.step(f'Проверка видимости {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            return locator.is_visible()