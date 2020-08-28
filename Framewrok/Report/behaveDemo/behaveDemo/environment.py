from behave import fixture, use_fixture
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType


@fixture
def selenium_browser(context):
    config_browser = context.config.userdata["browser"]
    if config_browser == "chrome":
        context.browser = webdriver.Chrome()
    else:
        context.browser = webdriver.Ie()
    context.browser.maximize_window()
    yield context.browser
    context.browser.quit()


def before_scenario(context, scenario):
    use_fixture(selenium_browser, context)


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.browser.get_screenshot_as_png(), 'screenshot', attachment_type=AttachmentType.PNG)

