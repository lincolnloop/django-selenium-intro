import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

try:
    from selenium_intro.local_settings import SELENIUM_WEBDRIVER
except:
    from selenium.webdriver.firefox import webdriver as SELENIUM_WEBDRIVER

class CustomWebDriver(SELENIUM_WEBDRIVER.WebDriver):
    """Our own WebDriver with some helpers added"""

    def find_css(self, css_selector):
        """Shortcut to find elements by CSS. Returns either a list or singleton"""
        elems = self.find_elements_by_css_selector(css_selector)
        found = len(elems)
        if found == 1:
            return elems[0]
        elif not elems:
            raise NoSuchElementException(css_selector)
        return elems
