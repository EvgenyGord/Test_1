import pytest

@pytest.fixture(scope="session")
def browser():
    with pytest.raises(Exception, match="Could not start playwright"):
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            yield p.chromium.launch(headless=True)