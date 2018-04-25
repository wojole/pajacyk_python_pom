from pajacykLocators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Pajacyk" appears in page title"""
        return "Pajacyk" in self.driver.title

    def click_belly_button(self):
        """Triggers clicks counter"""
        element = self.driver.find_element(*MainPageLocators.JAK_POMAGAC)
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, -504, 0).click().perform()

    def wait_for_ads_to_load(self):
        """Wait for right banner to load to ensure that visit is counted"""
        element = self.driver.find_element(*MainPageLocators.BANNER_PRAWA)
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of(element))


