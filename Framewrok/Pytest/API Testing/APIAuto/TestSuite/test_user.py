#!/usr/bin/python
# -*- coding: <encoding name> -*-

# @Author  : Janey Zhou
# @Time    : 2020/03/16 10:54
# @File    : xxxxxxxxxxx.py
# @Project : xxxxxxxxxxxxx
# @Desc    : xxxxxxxxxxxxxxxxx
import json

import pytest

from APIAuto.Config.APIConfig import cfg
from APIAuto.Scripts.Case import get_case, compare_result
from APIAuto.Scripts.core_employee import create_user, find_employee_from_list, delete_employee
from APIAuto.Utils.Logger import logger


def setup_module(module):
	logger.info("setup_module()")


def teardown_module(module):
	logger.info("teardown_module()")


class TestUser:
	case_path = cfg.Employee_Test_Data_Path
	@classmethod
	def setup_class(cls):
		logger.info('setup_class()')

	@classmethod
	def teardown_class(cls):
		logger.info("teardown_class()")

	def setup_method(self, method):
		logger.info('setup_method()')

	def teardown_method(self):
		logger.info("teardown_method()")

	@pytest.mark.smoke
	@pytest.mark.parametrize('case', get_case(path=case_path, file_name="users.case"))
	def test_create_user(self, case):
		logger.info("Start running test case: {}".format(case["Title"]))

		# Create a new employee and verify the new employeed's information is right
		new_user = create_user(case["Input"])
		assert new_user["status"] == "success"
		assert compare_result(case["Output"], new_user["data"])

		# Verify the new employee could be find from all employee list
		new_user_id = new_user["data"]["id"]
		logger.info("the new empolyee id is {}".format(new_user_id))
		assert find_employee_from_list(new_user_id), "new user does not exist in the employee list"

		# Delete the new employee and verify the deleted employee could not be found from employee list
		delete_employee(new_user_id)
		assert not (find_employee_from_list(new_user_id)), "new user does not be deleted from the employee list"

	@pytest.mark.skip
	def test_delete_user(self):
		logger.info("delete user")