import time
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from selenium_intro.selenium_tests.test import SeleniumTestCase
from selenium_intro.selenium_tests.webdriver import CustomWebDriver

# Make sure your class inherits from your base class
class Auth(SeleniumTestCase):
        
    def setUp(self):
        # setUp is where you setup call fixture creation scripts
        # and instantiate the WebDriver, which in turns loads up the browser.
        User.objects.create_superuser(username='admin',
                                      password='pw',
                                      email='info@lincolnloop.com')
        
        # Instantiating the WebDriver will load your browser
        self.wd = CustomWebDriver()

    def tearDown(self):
        # Don't forget to call quit on your webdriver, so that
        # the browser is closed after the tests are ran
        self.wd.quit()

    # Just like Django tests, any method that is a Selenium test should
    # start with the "test_" prefix.
    def test_login(self):
        """
        Django Admin login test
        """
        # Open the admin index page
        self.open(reverse('admin:index'))
        
        # Selenium knows it has to wait for page loads (except for AJAX requests)
        # so we don't need to do anything about that, and can just
        # call find_css. Since we can chain methods, we can
        # call the built-in send_keys method right away to change the
        # value of the field
        self.wd.find_css('#id_username').send_keys("admin")
        # for the password, we can now just call find_css since we know the page
        # has been rendered
        self.wd.find_css("#id_password").send_keys('pw')
        # You're not limited to CSS selectors only, check
        # http://seleniumhq.org/docs/03_webdriver.html for 
        # a more compreehensive documentation.
        self.wd.find_element_by_xpath('//input[@value="Log in"]').click()
        # Again, after submiting the form, we'll use the find_css helper
        # method and pass as a CSS selector, an id that will only exist
        # on the index page and not the login page
        self.wd.find_css("#content-main")
