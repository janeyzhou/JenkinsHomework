import logging
import time

from behave import given, when, then, use_fixture

from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage


@given("a set of valid user account")
def get_user_account(context):
    context.username = context.table[0][0]
    context.password = context.table[0][1]
    logging.info("User account is {}/{}".format(context.username, context.password))


@when("I login without username")
def login_without_username(context):
    try:
        logging.info("Login with out username")
        context.login_page = LoginPage(context.driver)
        context.login_page.go_to_page(LoginPage.url, LoginPage.title)
        context.login_page.negative_login(username='', password=context.password)
    except Exception as e:
        logging.error(e)
        raise e


@then("I should see the alert message")
def check_error_message(context):
    try:
        logging.info("Verify alert message")
        message = context.text.strip()
        context.login_page.verify_alert_message(message)
    except Exception as e:
        logging.error(e)
        raise e


@given("I am not logged in")
def check_cookies(context):
    try:
        logging.info("Check cookies")
        cookies = context.driver.get_cookies()
        if cookies:
            logging.info("Delete cookies")
            context.driver.delete_all_cookies()
        else:
            logging.info("you are not logged in, please continue")
    except Exception as e:
        logging.error(e)
        raise e


@when('I login with valid account "{username}" "{password}"')
def login_with_valid_account(context, username, password):
    try:
        context.username = username
        context.password = password
        login_page = LoginPage(context.driver)
        login_page.go_to_page(LoginPage.url, LoginPage.title)
        login_page.login(context.username, context.password)
    except Exception as e:
        logging.error(e)
        raise e


@then("I should login successfully")
def verify_greeting(context):
    try:
        home_page = HomePage(context.driver)
        home_page.verify_greeting(context.username)
    except Exception as e:
        logging.error(e)
        raise e
