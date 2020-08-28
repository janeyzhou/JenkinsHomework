import datetime
import json
import logging
import os
import threading

from behave import use_fixture
from behave.model_core import Status

from PageObject.BasePage import InitWebDriver
from Utils import Logger
from Utils.Common import get_test_data, get_current_datetime, take_screenshot, read_log
from bengoframe.report_creator import ReportCreator
from bengoframe.tests_appender import TestAppender

suite_name = 'Behave - Work Item'
log_level = "INFO"
thread_count = "1"
re_run = "No"


def before_all(context):
    context.report_path = 'Report/{}'.format(get_current_datetime())
    os.makedirs(context.report_path)

    Logger.init_logging(context.report_path)

    logging.info("Init Report Creator")
    context.reporter = ReportCreator(suite_name=suite_name, grid_address='', log_level=log_level,
                                     thread_count=thread_count, database='', re_run=re_run,
                                     output_path=context.report_path)

    logging.info("Create screenshot folder")
    context.screenshot_path = '{}/tempScreenShort'.format(context.report_path)
    os.makedirs(context.screenshot_path)

    logging.info("Get test date")
    context.test_data = get_test_data('TestData/case_data.json')


def before_feature(context, feature):
    logging.info("start before feature ...")


def before_scenario(context, scenario):
    logging.info("Start before scenario ...")
    logging.info("Set step to continue when raise exception")
    scenario.continue_after_failed_step = True
    context.scenario = scenario.name
    logging.info("Init driver")
    context.driver = InitWebDriver.getWebDriver('Chrome')

    context.appender = TestAppender(test_name=scenario.name, feature_name=context.feature.name,
                                    reporter=context.reporter)

    context.reporter.set_appender(scenario.name, context.appender)


def before_step(context, step):
    logging.info("Set thread name to scenario and step name")
    context.thread_name = context.scenario + '/' + step.name
    threading.current_thread().setName(context.thread_name)


def after_step(context, step):
    data = json.dumps(context.test_data)
    step_log = read_log(context.report_path, context.thread_name)
    if step.status == Status.failed:
        failed_screenshot = take_screenshot(context.driver, context.screenshot_path)
        context.appender.appender_step(step_status="failed",
                                       step_description=step.name, use_data=data, step_details=step_log,
                                       screenshot_name=failed_screenshot)
    elif step.status == Status.passed:
        context.appender.appender_step(step_status="passed",
                                       step_description=step.name, use_data=data, step_details=step_log)


def after_scenario(context, scenario):
    logging.info("Start after scenario ...")
    threading.currentThread().setName("MainThread")
    logging.info("Quite driver after scenario")
    context.driver.quit()

    context.appender.completed()


def after_feature(context, feature):
    logging.info("Start after feature ...")


def after_all(context):
    logging.info("Start after all ...")
    context.reporter.completed(screenshot_folder=context.screenshot_path)
