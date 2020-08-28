#!/usr/bin/python
# -*- coding: <encoding name> -*-

import json
import os
import csv

import re

from deepdiff import DeepDiff

from APIAuto.Config.APIConfig import cfg
from APIAuto.Utils.Logger import logger


class Case:
    def __init__(self, case_path):
        current_dir = os.path.dirname(__file__)
        self.case_relative_path = os.path.join(current_dir, "..", case_path)
        # with open(case_file_path, 'r') as case_file:
        #     self.reader = csv.DictReader(case_file)

    def get_all_input_files(self, case_name):
        case_file_full_path = os.path.join(self.case_relative_path, case_name)
        with open(case_file_full_path, 'r') as case_file:
            reader = csv.DictReader(case_file)
            input_file_list = []
            for row in reader:
                input_file_list.append(row["payload"])
        return input_file_list


def get_exp_data(path, exp_file_name):
    current_dir = os.path.dirname(__file__)
    exp_relative_path = os.path.join(current_dir, "..", path, exp_file_name)
    with open(exp_relative_path, 'r') as exp:
        reader = json.load(exp)
    return reader

def get_case(path, file_name):
    current_dir = os.path.dirname(__file__)
    case_relative_path = os.path.join(current_dir, "..", path, file_name)
    with open(case_relative_path, newline='') as data_file:
        data = csv.DictReader(data_file, delimiter=',')
        case = list(data)
        data_file.close()
    return case

def compare(exp, act, extra_skip_field=[]):
    default_skipped_fields = r'id'
    final_skipped_fields = default_skipped_fields
    if extra_skip_field:
        for item in extra_skip_field:
            final_skipped_fields = final_skipped_fields + '|' + item

    exclude_regex_paths = re.compile(final_skipped_fields)
    dpdiff = DeepDiff(exp, act, exclude_regex_paths=[exclude_regex_paths], ignore_order=True, report_repetition=True)
    if dpdiff == {}:
        result = True
    else:
        logger.error('comparing expected result with actual result failed. Here is the difference:')
        logger.error(dpdiff)
        result = False
    return result

def compare_result(output, actual):
    flag = False
    exp_data = json.loads(output)
    for k in exp_data["data"]:
        if actual[k] == exp_data["data"][k]:
            flag = True
        else:
            logger.error("comparing output with actual result failed on {}".format(k))
            flag = False
    return flag



steps = get_case("TestData/EmployeeModule", "users.case")
print(steps)
flag =False
print(not(flag))
assert not(flag)

case_path = cfg.Employee_Test_Data_Path

print(type(case_path))
print(case_path)
