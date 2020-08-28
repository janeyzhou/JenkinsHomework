from behave import given, when, then
import logging
import time
from behave import use_fixture
from features.fixtures import take_screenshot


@given('I have a valid account')
def init_account(context):
    context.username = "aaa@test.com"
    context.password = "123456"
    logging.info(f"Have user name {context.username}")
    logging.info(f"Have user name {context.password}")


@given('I am not logged in')
def not_logged_in(context):
    try:
        cookies = context.driver.get_cookies()
        if not cookies:
            logging.info("Cookies all clear, we are not logged in")
        else:
            logging.info(f"Cookies not all clear, Please check {cookies}")
    except Exception as e:
        logging.error(e)


@when('I navigate to the home page')
def navigate_to_home_page(context):
    try:
        context.driver.get("https://acme-test.uipath.com/account/login")
        time.sleep(2)
        current_title = context.driver.title
        use_fixture(take_screenshot, context)
        if "ACME System" in current_title:
            logging.info(f"We're in {current_title} page")
        else:
            logging.info("We're not in home page")
    except Exception as e:
        logging.error(e)


@then('I should see the login form')
def see_login_form(context):
    try:
        login_btn = context.driver.find_element_by_id("buttonLogin")
        # forgotPwdBtn ...
        # registerBtn ...
        # emailField ...
        # pwdField  ...
    except Exception as e:
        logging.info("Login form may not exit in this page")
        logging.error(f"Please check the error message {e}")


@when('I fill in username')
def input_username(context):
    username = context.username
    try:
        emailField = context.driver.find_element_by_id("email")
        emailField.send_keys(username)
    except Exception as e:
        logging.info("Email field may not exit in this page")
        logging.error(f"Please check the error message {e}")


@when('I press login button')
def press_login_btn(context):
    try:
        login_btn = context.driver.find_element_by_id("buttonLogin")
        login_btn.click()
        time.sleep(1)
    except Exception as e:
        logging.info("Login button may not exit in this page")
        logging.error(f"Please check the error message {e}")


@then('I should see the alert contains correct text')
def see_alert_message(context):
    try:
        expect_text = context.text.strip()
        time.sleep(1)
        actual_text = context.driver.switch_to.alert.text
        if actual_text in expect_text:
            logging.info(f"Alert message was correct with text: {expect_text}")
        else:
            logging.info(f"Alert message was not correct. "
                         f"Actual text is: {actual_text}, Expect text is: {expect_text}")
        context.driver.switch_to.alert.accept()
    except Exception as e:
        logging.error(f"Please check the error message {e}")
