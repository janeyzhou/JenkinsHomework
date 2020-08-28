from .base_page import BasePage
from selenium.webdriver.common.by import By
from libs.action import Action


class LoginPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser)
        self.user_name_locator = (By.ID, 'username_field')
        self.password_locator = (By.ID, 'password_field')
        self.login_button_locator = (By.ID, 'login_button')

    def input_user_name(self, text):
        Action.input_text(self.browser, self.user_name_locator, text)

    def input_password(self, text):
        Action.input_text(self.browser, self.password_locator, text)

    def click_login_button(self):
        Action.click_button(self.browser, self.login_button_locator)