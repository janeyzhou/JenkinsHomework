import json
import os
import time
import uuid
from datetime import datetime


def get_test_data(file_path):
    path = os.path.join(os.path.dirname(__file__), '..', file_path)
    with open(file_path, 'r') as f:
        test_data = json.load(f)
        f.close()
    return test_data


def get_uuid():
    return str(uuid.uuid1()).replace("-", "").upper()


def get_current_datetime():
    curr_time = datetime.now()
    str_time = datetime.strftime(curr_time, '%Y-%m-%d-%H-%M-%S')
    return str_time


def take_screenshot(driver, path):
    screenshot_path = os.path.join(os.path.dirname(__file__), '..', path)
    screenshot_name = "{}.png".format(get_uuid())
    driver.save_screenshot("{}/{}".format(screenshot_path, screenshot_name))
    time.sleep(2)
    return screenshot_name


def read_log(path, thread_name=''):
    log_file = "{}/behave_log.log".format(path)
    full_path = os.path.join(os.path.dirname(__file__), '..', log_file)
    log = ''
    for line in open(full_path):
        if thread_name in line:
            log = log + line
    return log

