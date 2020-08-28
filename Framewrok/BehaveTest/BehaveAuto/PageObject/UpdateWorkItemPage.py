import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.BasePage import BasePage


class UpdateWorkItemPage(BasePage):
    update_work_item_loc = (By.CSS_SELECTOR, ".panel-heading")
    new_status_loc = (By.ID, "newStatus")
    add_comments_loc = (By.ID, 'newComment')
    update_work_item_button_loc = (By.ID, 'buttonUpdate')
    work_item_detail_loc = (By.CSS_SELECTOR, "div[class='container-fluid'] div[class='col-lg-12']>p")

    def is_displayed_update_work_item(self):
        is_displayed = self.is_element_displayed(self.update_work_item_loc)
        assert is_displayed, "Update work item section does not display on update work item page"

    def get_work_item_details(self):
        work_item_detail = self.find_element(self.work_item_detail_loc).text
        return work_item_detail

    def get_wiid(self):
        work_item_info = self.get_work_item_details()
        work_item_info_list = work_item_info.split()
        return work_item_info_list[1]

    # def add_comments(self, comment):
    #     self.input_text(self.add_comments_loc, comment)
    #
    # def set_new_status(self, status_value):
    #     Select(self.find_element(self.new_status_loc)).select_by_value(status_value)
    #
    # def click_update_work_item_button(self):
    #     self.click(self.update_work_item_button_loc)

    def update_work_item(self, comments, status):
        self.input_text(self.add_comments_loc, comments)
        Select(self.driver.find_element(*self.new_status_loc)).select_by_value(status)
        self.click(self.update_work_item_button_loc)
        time.sleep(2)
        alert_message = self.get_alert_message()
        assert alert_message == "Work Item was updated accordingly", "Failed to update work item, alert message is '{}'".format(alert_message)

    # def get_alter_message(self):
    #     alert = self.driver.switch_to.alert
    #     message = alert.text
    #     alert.accept()
    #     return message
    #
    # # def switch_to_work_item_details_page(self):
    # #     self.swith_to_window(int('-2'))
