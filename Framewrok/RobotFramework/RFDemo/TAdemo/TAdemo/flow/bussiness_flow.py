from pages.login_page import LoginPage


class LoginFlow:
    def __init__(self, browser):
        self.login_page = LoginPage(browser)

    def login_with_account(self, username, password):
        self.login_page.input_user_name(username)
        self.login_page.input_password(password)
        self.login_page.click_login_button()
