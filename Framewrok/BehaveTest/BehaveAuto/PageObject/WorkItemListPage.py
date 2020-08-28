import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from PageObject.BasePage import BasePage
from PageObject.WorkItemDetailPage import WorkItemDetailPage


class WorkItemListPage(BasePage):
    title = 'ACME System 1 - Work Items'
    url = 'https://acme-test.uipath.com/work-items'

    work_items_loc = (By.CSS_SELECTOR, ".table tr")

    sarch_button_loc = (By.CSS_SELECTOR, ".table tr td:nth-child(1) a:nth-child(1)")
    wiid_loc = (By.CSS_SELECTOR, ".table tr td:nth-child(2)")
    status_loc = (By.CSS_SELECTOR, ".table tr td:nth-child(5)")

    def get_wiid(self, index):
        wiid_element = self.find_elements(self.wiid_loc)
        wiid_list = []
        for element in wiid_element:
            wiid_list.append(element.text)
        return wiid_list[index - 1]

    def get_status(self, index):
        status_element = self.find_elements(self.status_loc)
        status_list = []
        for element in status_element:
            status_list.append(element.text)
        return status_list[index - 1]

    def verify_status(self, index, status):
        actual_status = self.get_status(index)
        assert actual_status == status, "The latest work item status for row {} is {}, it should be {}".format(index, actual_status, status)

    def click_one_work_item(self, driver, index):
        search_button_elements = self.find_elements(self.sarch_button_loc)
        expected_wiid = self.get_wiid(index)
        search_button_elements[index - 1].click()

        work_item_detail_page = WorkItemDetailPage(driver)
        work_item_detail_page.is_displayed_work_item_details()
        actual_wiid = work_item_detail_page.get_wiid()
        assert actual_wiid == expected_wiid, "Failed to open work item detail page for WIID {}".format(expected_wiid)
