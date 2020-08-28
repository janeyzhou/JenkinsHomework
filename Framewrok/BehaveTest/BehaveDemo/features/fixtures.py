from behave import fixture
from selenium import webdriver
import time
import os
import logging
import uuid


@fixture
def browser_chrome(context, host_port):
    caps = webdriver.DesiredCapabilities.CHROME.copy()
    browser = webdriver.Remote(
        desired_capabilities=caps, command_executor="{}/wd/hub".format(host_port))
    browser.implicitly_wait(2)
    context.browser = browser
    browser.find_element()
    return browser


@fixture
def take_screenshot(context):
    try:
        # File_Path = os.getcwd()
        # scenario_name = context.scenario.name
        # current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        # out_path = f"{File_Path}\\{scenario_name}"
        # if not os.path.exists(out_path):
        # os.makedirs(out_path)
        # out_file = f"{out_path}/{current_time}.png"
        out_path = context.report_path
        logging.info(out_path)
        out_file = f"{out_path}/{get_uuid()}.png"
        context.driver.save_screenshot(out_file)
        time.sleep(1)
    except Exception as e:
        logging.error(e)


def get_uuid():
    return str(uuid.uuid1()).replace("-", "").upper()
