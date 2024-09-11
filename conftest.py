import pytest

from base.pages.buttons.buttons_page import ButtonsPage
from base.pages.date_picker.date_picker_page import Date_Picker
from base.pages.login.login_page import Login
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogs
from base.pages.practice_form.practice_form_page import PracticeFormPage
from base.pages.radiobutton.radiobutton_page import RadioButtonPage
from base.pages.select_menu.select_menu_page import Select_Menu
from base.pages.textbox.textbox_page import TextboxPage
from base.pages.checkbox.checkbox_page import CheckboxPage
from base.pages.upload_and_download.upload_and_download_page import Upload_and_Download_Page
from src.config.playwright import PlaywrightConfig
from playwright.sync_api import Page, sync_playwright, Browser


@pytest.fixture()
def page() -> Page:
    with sync_playwright() as playwright:
        browser = get_browser(playwright)
        page = browser.new_page(viewport=PlaywrightConfig.PAGE_VIEWPORT_SIZE)
        yield page
        browser.close()

def get_browser(playwright) -> Browser:
    browser_type = playwright.chromium if PlaywrightConfig.BROWSER == 'chrome' else playwright.firefox
    return browser_type.launch(
        headless=PlaywrightConfig.IS_HEADLESS,
        slow_mo=PlaywrightConfig.SLOW_MO
    )

@pytest.fixture(scope='function')
def practice_form(page: Page) -> PracticeFormPage:
    return PracticeFormPage(page)


@pytest.fixture(scope='function')
def textbox(page: Page) -> TextboxPage:
    return TextboxPage(page)

@pytest.fixture(scope='function')
def checkbox(page: Page) -> CheckboxPage:
    return CheckboxPage(page)

@pytest.fixture(scope='function')
def radiobutton(page: Page) -> RadioButtonPage:
    return RadioButtonPage(page)

@pytest.fixture(scope='function')
def buttons(page: Page) -> ButtonsPage:
    return ButtonsPage(page)

@pytest.fixture(scope='function')
def upload_and_download(page: Page) -> Upload_and_Download_Page:
    return Upload_and_Download_Page(page)

@pytest.fixture(scope='function')
def modal_dialogs(page: Page) -> ModalDialogs:
    return ModalDialogs(page)

@pytest.fixture(scope='function')
def date_picker(page: Page) -> Date_Picker:
    return Date_Picker(page)

@pytest.fixture(scope='function')
def select_menu(page: Page) -> Select_Menu:
    return Select_Menu(page)

@pytest.fixture(scope='function')
def login(page: Page) -> Login:
    return Login(page)