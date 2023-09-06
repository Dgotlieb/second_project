import unittest
from selenium import webdriver
from pages.home_page import Homepage
from pages.logged_in_home_page import LoggedInHomePage

class Homepage(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get("https://buyme.co.il/")

    def click_sign_in_button(self):
        self.driver.find_element_by_css_selector("<li class='notSigned' data-ember-action='1012'>")

class LoggedInHomePage(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver

    def assert_logged_in_home_page(self):
        assert self.driver.find_element_by_id(
            "<button id='ember1921' type='submit' gtm='כניסה ל-BUYME' class='ember-view bm-btn no-reverse main md "
            "stretch' uabtn='true'><span class='label' andiallelmwithtext='14'>כניסה ל-BUYME</span></button>")

driver = webdriver.Chrome()
home_page = Homepage(driver)
home_page.go_to_home_page()
home_page.click_sign_in_button()
logged_in_home_page = LoggedInHomePage(driver)
logged_in_home_page.assert_logged_in_home_page()
driver.quit()

