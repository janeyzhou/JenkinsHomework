import os
import time
from lib2to3.pgen2 import driver
from operator import is_not

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_elements(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def is_element_displayed(self, locator):
        self.wait_elements(locator)
        elements = self.find_elements(locator)
        if len(elements) > 0:
            return True
        else:
            return False

    def input_text(self, locator, text):
        self.wait_elements(locator)
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        self.wait_elements(locator)
        self.find_element(locator).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_element_attribute(self, locator, attribute_type):
        return self.find_element(locator).get_attribute(attribute_type)

    def close_browser(self):
        self.driver.close()

    def switch_to_window(self, index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])

