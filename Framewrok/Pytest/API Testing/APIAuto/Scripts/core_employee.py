#!/usr/bin/python
# -*- coding: <encoding name> -*-

# @Author  : Janey Zhou
# @Time    : 2020/03/16 10:54
# @File    : xxxxxxxxxxx.py
# @Project : xxxxxxxxxxxxx
# @Desc    : xxxxxxxxxxxxxxxxx


import json

import pytest
import requests

from APIAuto.Config.APIConfig import cfg
from APIAuto.Scripts.Case import get_case
from APIAuto.Scripts.endPoint import endPoint
from APIAuto.Utils.Logger import logger


def request():
	session = requests.session()
	requests.utils.add_dict_to_cookiejar(session.cookies, endPoint.COOKIES)
	return session


def create_user(user_info):
	logger.info("create a new employee")
	# 这里我们可以设置user template，需要测试的数据写入input就可以了，其他的不测字段使用user template中的值
	user = {
		"name": "test1",
		"salary": "1000",
		"age": "25"
	}
	input = json.loads(user_info)
	for k in input:
		user[k] = input[k]
	response = request().post("http://dummy.restapiexample.com/api/v1/create", headers=endPoint.HEADERS,
	                         json=user).json()
	return response


def get_all_employee():
	# logger.info("Get all employees")
	response = request().get("http://dummy.restapiexample.com/api/v1/employees", headers=endPoint.HEADERS).json()
	return response


def delete_employee(id):
	logger.info("Delete an employee with id: {}".format(id))
	url = cfg.domain + endPoint.DELETE_USER + "{}".format(id)
	request().delete(url=url, headers=endPoint.HEADERS)


def find_employee_from_list(user_id):
	employees = get_all_employee()
	flag = False
	for item in employees["data"]:
		if int(item["id"]) == user_id:
			logger.info("Find an employee with id: {} from employee list".format(user_id))
			flag = True
	return flag
