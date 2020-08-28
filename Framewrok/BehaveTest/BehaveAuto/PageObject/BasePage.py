import logging
import time

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class InitWebDriver:
    def getWebDriver(self, driver_type='Chrome'):
        if driver_type == 'Chrome':
            return webdriver.Chrome("C:/driver/chromedriver.exe")
        elif driver_type == 'Firefox':
            return webdriver.Firefox("../Driver/firefoxdriver.exe")
        else:
            raise Exception("Driver type {} is not supported".format(driver_type))


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def find_element(self, locator):
        self.wait_element(locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        self.wait_elements(locator)
        return self.driver.find_elements(*locator)

    def wait_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_elements(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located)

    def is_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def swith_to_window(self, index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])

    def go_to_page(self, url, title):
        self.driver.get(url)
        time.sleep(2)
        logging.info(self.driver.title)
        logging.info(title)
        assert self.driver.title == title, "Failed to open page {}".format(url)


    def check_cookie(self):
        cookies = self.driver.get_cookies()
        if cookies:
            logging.warning("Cookies not clear, please clear cookies")
            logging.info("Start Delete cookies")
            self.driver.delete_all_cookies()
        else:
            logging.info("Cookies clear, please continue")

    def get_alert_message(self):
        alert = self.driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message


