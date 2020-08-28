import logging
import time

from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage
from PageObject.ResetTestDataPage import ResetTestDataPage
from PageObject.WorkItemListPage import WorkItemListPage


class HomePage(BasePage):
    url = 'https://acme-test.uipath.com'
    title = 'ACME System 1 - Dashboard'

    greeting_loc = (By.CSS_SELECTOR, "div[class= 'main-container'] h1")
    work_items_button_loc = (By.CSS_SELECTOR, "div[class='dropdown']:nth-child(2) button")
    user_options_loc = (By.CSS_SELECTOR, ".dropdown:nth-child(1) button")
    reset_test_data_button_loc = (By.CSS_SELECTOR, ".dropdown:nth-child(1) li:nth-child(2)")

    def click_work_items_button(self):
        self.click(self.work_items_button_loc)
        time.sleep(2)
        assert self.driver.title == WorkItemListPage.title, "Failed to redirect to work item list page after clicking 'Work Items' button"

    def verify_greeting(self, email):
        greeting = self.find_element(self.greeting_loc).get_attribute("innerHTML")
        assert email in greeting, "{} does not display in greeting, login failed with account {}".format(email, email)

    def click_reset_test_data_button(self):
        self.click(self.user_options_loc)
        is_displayed = self.find_element(self.user_options_loc).get_attribute('aria-expanded')
        assert is_displayed == 'true', "Sub menus of User options button does not appear on UI"
        self.click(self.reset_test_data_button_loc)
        time.sleep(2)
        assert self.driver.title == ResetTestDataPage.title, "Failed to redirect to reset test data page after clicking 'Reset Test Data' button"

