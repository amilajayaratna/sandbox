import pytest

from pages.search import DuckDuckGoSearchPage
from pages.results import DuckDuckGoResultsPage
from selenium.webdriver import Chrome

@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_basic_search(browser):
    PHRASE = "panda"
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    results_page = DuckDuckGoResultsPage(browser)
    title = results_page.get_title()

    assert title == f"{PHRASE} at DuckDuckGo"