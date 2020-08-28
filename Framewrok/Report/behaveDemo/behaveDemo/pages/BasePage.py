from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from hamcrest import *


class wait_for_the_attribute_value(object):
    def __init__(self, locator, attribute, value):
        self.locator = locator
        self.attribute = attribute
        self.value = value

    def __call__(self, driver):
        try:
            element_attribute = EC._find_element(driver, self.locator).get_attribute(self.attribute)
            return element_attribute == self.value
        except EC.StaleElementReferenceException:
            return False


class Page(object):
    # header page object
    # LOGO = (By.CSS_SELECTOR, 'a[id="logo"]')
    # CMS_DASHBOARD = (By.CSS_SELECTOR, 'div.nav_bar li:nth-child(1)')
    # TMS_DASHBOARD = (By.CSS_SELECTOR, 'div.nav_bar li:nth-child(2)')
    # SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, 'div[class="mini-toastr__notification -info"] div')
    # ERROR_NOTIFICATION = (By.CSS_SELECTOR, 'div[class="mini-toastr__notification -error"] div')
    # MASK = (By.CSS_SELECTOR, 'div.mask')
    # DROPDOWN_MENU_BUTTON = (By.CSS_SELECTOR, 'ul[id="dropdown-menu"]')
    # DROPDOWN_MENU = (By.CSS_SELECTOR, 'ul.is-dropdown-submenu')
    # LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a[id="logout"]')

    def __init__(self, driver):
        self.driver = driver
        # self.header_locator = HeaderLocators

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_displayed(self, locator):
        # time.sleep(2)
        enable = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        assert_that(enable, is_not(False))
        # return self.find_element(locator).is_displayed()

    def input_text_element(self, locator, text):
        text_element = self.find_element(locator)
        text_element.clear()
        text_element.send_keys(text)

    def click(self, locator):
        element = WebDriverWait(self.driver, 5, 1).until(EC.element_to_be_clickable(locator))
        # element = self.find_element(locator)
        element.click()

    def is_active(self, locator):
        # time.sleep(2)
        # enable = WebDriverWait(self.driver, 5).until(wait_for_the_attribute_value(locator, "active", "true"))
        # assert_that(enable, equal_to(True))
        self.attribute_verified(locator, "active", "true")

    def attribute_verified(self, locator, attribute, expected):
        # time.sleep(2)
        enable = WebDriverWait(self.driver, 5).until(wait_for_the_attribute_value(locator, attribute, expected))
        assert_that(enable, equal_to(True))

    def checkbox_is_selected(self, locator, status):
        enable = WebDriverWait(self.driver, 5).until(EC.element_located_selection_state_to_be(locator, status))
        assert_that(enable, equal_to(True))

    def is_not_visible(self, locator, timeout=5):
        enable = WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(locator))
        assert_that(enable, equal_to(True))

    def is_success_notification_dismiss(self):
        self.is_not_visible(self.SUCCESS_NOTIFICATION)

    def assert_to_equal(self, expect, actual):
        assert_that(actual, equal_to(expect))

    def logout(self):
        self.click(self.DROPDOWN_MENU_BUTTON)
        self.is_displayed(self.DROPDOWN_MENU)
        self.click(self.LOGOUT_BUTTON)
        self.is_not_visible(self.MASK)
