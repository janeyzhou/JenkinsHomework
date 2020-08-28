import logging
import time

from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class ResetTestDataPage(BasePage):
    title = 'ACME System 1 - Account - Reset Test Data'
    url = 'https://acme-test.uipath.com/reset-test-data'
    reset_test_data_button_loc = (By.CSS_SELECTOR, "button[id ='buttonRTD']")

    def reset_test_data(self):
        self.click(self.reset_test_data_button_loc)
        time.sleep(2)
        message = self.get_alert_message()
        assert message == 'Your Test Data has been successfully reset.', "Failed to reset test data"

