import json

from Logger import logger

class myLibrary:

    def __init__(self):
        pass

    def compare_result(self, exp, act):
        flag = False
        # exp_data = json.loads(exp)
        # act_data = json.loads(act)
        for k in exp:
            if act["data"][k] == exp[k]:
                flag = True
            else:
                logger.error("comparing actual result with expected data failed on {}".format(k))
                flag = False
        return flag

    def is_new_user_displayed(self, employees, new_id):
        # employee_list = json.loads(employees)
        flag = False
        for item in employees["data"]:
            if str(item["id"]) == new_id:
                logger.info("Find an employee with id: {} from employee list".format(new_id))
                flag = True
        return flag

