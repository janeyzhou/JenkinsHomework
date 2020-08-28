import os
import time
import logging
import shutil
import threading
from selenium import webdriver
from datetime import datetime
from bengoframe.report_creator import ReportCreator
from bengoframe.tests_appender import TestAppender

suite_name = "Behave"
grid_address = "http://localhost:4444/wd/hub"
log_level = "INFO"
thread_count = "1"
database = "Behave-QA"
re_run = "No"


def before_all(context):
    sub_path = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    context.report_path = f"report/{sub_path}"
    os.makedirs(context.report_path, exist_ok=True)
    # -------------------------------Report Creator Init--------------------------------------------------#
    context.temp_screenshot_path = f"report/{sub_path}/temp_screenshot"
    os.makedirs(context.temp_screenshot_path, exist_ok=True)
    context.reporter = ReportCreator(suite_name=suite_name, grid_address=grid_address, log_level=log_level,
                                     thread_count=thread_count, database=database, re_run=re_run,
                                     output_path=context.report_path)
    logging.info("I will run before the all")


def before_feature(context, feature):
    logging.info("I will run before the feature")


def before_tag(context, tag):
    logging.info("I will run before the tag")


def before_scenario(context, scenario):
    threading.current_thread().setName(scenario.name)
    context.appender = TestAppender(test_name=scenario.name, feature_name=context.feature.name,
                                    reporter=context.reporter)
    context.reporter.set_appender(scenario.name, context.appender)
    caps = webdriver.DesiredCapabilities.CHROME.copy()
    context.driver = webdriver.Remote(
        desired_capabilities=caps, command_executor="http://localhost:4444/wd/hub")
    context.driver.implicitly_wait(20)
    context.appender.appender_step(step_status="passed",
                                   step_description="Init the webdriver before test",
                                   step_details=f"Create webdriver session on grid \n {grid_address}")
    logging.info("I will run before the scenario and with tags: " + str(scenario.tags))


# def before_step(context, step):
#     logging.info("I will run before the step")
#
#
# def after_step(context, step):
#     logging.info("I will run after the step")


def after_scenario(context, scenario):
    time.sleep(2)
    context.driver.quit()
    # Completed the test appender and close
    threading.current_thread().setName("MainThread")
    context.appender.completed()
    logging.info("I will run after the scenario")


# def after_tag(context, tag):
#     logging.info("I will run after the tag")
#
#
# def after_feature(context, feature):
#     logging.info("I will run after the feature")


def after_all(context):
    # Completed the reporter and close
    threading.current_thread().setName("MainThread")
    context.reporter.completed(context.temp_screenshot_path)
    shutil.rmtree(context.temp_screenshot_path)
    logging.info("I will run after the all")
