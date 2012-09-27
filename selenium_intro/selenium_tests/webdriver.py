import time
from selenium.common.exceptions import NoSuchElementException
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
    
    def wait_for_css(self, css_selector, timeout=10):
        """Wait for element to be visible in the DOM"""
        waited = 0
        while waited < timeout:
            try:
                elem = self.find_css(css_selector)
                assert elem and elem.is_displayed()
                return elem
            except (NoSuchElementException, AssertionError):
                waited += 1
                time.sleep(1)