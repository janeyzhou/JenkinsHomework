import logging
import time

from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage
from PageObject.UpdateWorkItemPage import UpdateWorkItemPage


class WorkItemDetailPage(BasePage):

    work_item_details_title_loc = (By.CSS_SELECTOR, ".col-lg-5:nth-child(2) h4")
    work_item_details_loc = (By.CSS_SELECTOR, "div[class='panel-body'] div[class='col-lg-5']:nth-child(2) p")
    update_button_loc = (By.CSS_SELECTOR, "div[class='panel-body'] div[class='col-lg-5']:nth-child(2) p button")

    def is_displayed_work_item_details(self):
        is_displayed = self.is_element_displayed(self.work_item_details_title_loc)
        assert is_displayed, "Work item detail section does not display on work item detail page"

    def get_work_item_detail(self):
        work_item_detail = self.find_element(self.work_item_details_loc).text
        return work_item_detail

    def get_wiid(self):
        work_item_detail = self.get_work_item_detail()
        work_item_list = work_item_detail.split()
        return work_item_list[1]

    def get_status(self):
        work_item_detail = self.get_work_item_detail()
        work_item_list = work_item_detail.splitlines()
        work_item = work_item_list[2].split()
        return work_item[1]

    def click_update_work_item_button(self):
        expected_wiid = self.get_wiid()
        self.click(self.update_button_loc)

        self.swith_to_window(int('-1'))
        update_work_item_page = UpdateWorkItemPage(self.driver)
        actual_wiid = update_work_item_page.get_wiid()
        update_work_item_page.is_displayed_update_work_item()
        assert actual_wiid == expected_wiid, "Failed to open update work item page for WIID {}".format(expected_wiid)


