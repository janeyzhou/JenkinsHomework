import logging
import time

from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage
from PageObject.HomePage import HomePage


class LoginPage(BasePage):
    title = 'ACME System 1 - Log In'
    url = 'https://acme-test.uipath.com/login'

    email_loc = (By.ID, 'email')
    password_loc = (By.ID, 'password')
    login_button_loc = (By.CSS_SELECTOR, "button[type='submit']")

    # def input_email(self, email_address):
    #     self.input_text(self.email_loc, email_address)
    #
    # def input_password(self, password):
    #     self.input_text(self.password_loc, password)
    #
    # def click_login_button(self):
    #     self.click(self.login_button_loc)

    def login(self, username, password):
        self.input_text(self.email_loc, username)
        self.input_text(self.password_loc, password)
        self.click(self.login_button_loc)
        time.sleep(2)
        current_title = self.driver.title
        assert current_title == HomePage.title, "Failed to login, Current title is {}, expected title is {}".format(
            current_title, HomePage.title)

    def negative_login(self, username, password):
        self.input_text(self.email_loc, username)
        self.input_text(self.password_loc, password)
        self.click(self.login_button_loc)
        time.sleep(2)

    def verify_alert_message(self, message):
        alert_message = self.get_alert_message()
        assert alert_message == message, "The alert message is wrong, please check '{}'".format(alert_message)
