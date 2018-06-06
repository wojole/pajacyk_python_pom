import unittest
from selenium import webdriver
import pajacykPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_module():

    global url
    url = "http://www.pajacyk.pl"


class PajacykPlSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def tests_pajacyk_pl(self):
        """
        Test is verifying page correctedness, clicks on button, waits for banner to load and exits browser.
        """

        # Load the main page. In this case the home page of pajacyk.pl.
        main_page = pajacykPage.MainPage(self.driver)
        # Checks if the word "Pajacyk" is in page title
        assert main_page.is_title_matches(), "pajacyk.pl title doesn't match."
        main_page.click_belly_button()
        main_page.wait_for_ads_to_load()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


class PajacykPlSearch_part2(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def tests_pajacyk_pl(self):
        """
        Test is verifying page correctedness, clicks on button, waits for banner to load and exits browser.
        """

        # Load the main page. In this case the home page of pajacyk.pl.
        main_page = pajacykPage.MainPage(self.driver)
        # Checks if the word "Pajacyk" is in page title
        assert main_page.is_title_matches(), "pajacyk.pl title doesn't match."
        main_page.click_belly_button()
        main_page.wait_for_ads_to_load()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


def teardown_module(self):
    global url
    self.driver = webdriver.Chrome()
    del url
    self.driver.get(url)
