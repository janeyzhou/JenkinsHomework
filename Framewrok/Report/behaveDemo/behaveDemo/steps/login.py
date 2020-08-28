from behave import *
from pages import *
from hamcrest import *
import ast


@given('I navigate to login page')
def step_impl(context):
    url = context.config.userdata["url"]
    context.browser.get(url)
    assert_that("Login Page", is_in(context.browser.title))


@then('I login with "{user}" and "{password}"')
def step_impl(context, user, password):
    login_page = LoginPage(context.browser)
    login_page.login_user(user, password)


@then('I login Successfully')
def step_impl(context):
    assert_that ("Welcome Page", is_in(context.browser.title) )