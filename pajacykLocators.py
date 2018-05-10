from selenium.webdriver.common.by import By



class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    JAK_POMAGAC = (By.XPATH, "/html/body/header/nav/ul/li[2]/a")
    KLIKI = (By.CSS_SELECTOR, 'html body div.dziekujemy.inactive div.table div.td div.p1 span.kliki')
    BANNER_PRAWA = (By.ID, 'banner_prawa')

