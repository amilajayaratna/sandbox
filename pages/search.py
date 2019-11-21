from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DuckDuckGoSearchPage:
    URL = 'http://www.duckduckgo.com'

    def __init__ (self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, what):
        user_input = self.browser.find_element(By.ID, 'search_form_input_homepage')
        user_input.send_keys(what + Keys.RETURN)