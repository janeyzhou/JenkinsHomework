import datetime
import logging
import os
import shutil
import threading
from concurrent.futures.thread import ThreadPoolExecutor

import allure
from allure_commons.types import AttachmentType
from behave import use_fixture
from behave.model_core import Status

from PageObject.BasePage import InitWebDriver
from Utils import Logger
from Utils.Common import get_test_data, get_current_datetime, take_screenshot, read_log

# from Utils.logging import logging


def before_all(context):
    logging.info("Create report folder")
    context.report_path = 'Report/{}'.format(get_current_datetime())
    os.makedirs(context.report_path)
    Logger.init_logging(context.report_path)


    logging.info("Create screenshot folder")
    context.screenshot_path = '{}/tempScreenShort'.format(context.report_path)
    os.makedirs(context.screenshot_path)

    logging.info("Get test date")
    context.test_data = get_test_data('TestData/case_data.json')


def before_feature(context, feature):
    logging.info("start before feature ...")


def before_scenario(context, scenario):
    logging.info("Set step to continue when raise exception")
    scenario.continue_after_failed_step = True

    logging.info("Start before scenario ...")

    logging.info("Init driver")
    context.driver = InitWebDriver.getWebDriver('Chrome')

    context.scenario = scenario.name


def before_step(context, step):
    context.thread_name = context.scenario + '/' + step.name
    threading.current_thread().setName(context.thread_name)


def after_step(context, step):
    data = "username: {}, password: {}".format(context.username, context.password)
    step_log = read_log(context.report_path, context.thread_name)
    if step.status == Status.failed:
        # failed_screenshot = take_screenshot(context.driver, context.screenshot_path)
        allure.attach(context.driver.get_screenshot_as_png(), 'screenshot', attachment_type=AttachmentType.PNG)


def after_scenario(context, scenario):
    logging.info("Start after scenario ...")
    logging.info("Quite driver after scenario")
    # context.driver.quit()

    logging.info("Set thread name as MainThread")
    threading.currentThread().setName("MainThread")




def after_feature(context, feature):
    logging.info("Start after feature ...")


def after_all(context):
    logging.info("Start after all ...")




