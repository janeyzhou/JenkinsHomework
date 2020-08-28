from .BasePage import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    USER_NAME = (By.ID, "username_field")
    PASSWORD = (By.ID, "password_field")
    LOGIN_BUTTON = (By.ID, "login_button")

    def __init__(self, driver):
        super().__init__(driver)

    def login_user(self, user, password):
        self.input_text_element(self.USER_NAME, user)
        self.input_text_element(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)


