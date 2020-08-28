from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Action():
    def __init__(self):
        pass

    @staticmethod
    def input_text(driver, locator, text):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            element.send_keys(text)
        except:
            print ("not able to locate " + str(locator))

    @staticmethod
    def click_button(driver, locator):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            element.click()
        except:
            print ("not able to locate " + str(locator))