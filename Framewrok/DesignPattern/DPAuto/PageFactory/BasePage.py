from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverFactory():
    @staticmethod
    def getWebDriver(browser='Chrome'):
        if browser == 'Chrome':
            return webdriver.Chrome("Driver/chromedriver.exe")
        elif browser == 'Firefox':
            return webdriver.firefox("../Driver/firefoxdriver.exe")
        elif browser == 'remote':
            return webdriver.remote("...")
        else:
            raise Exception("Browser {} does not exist".format(browser))


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 将元素的locator以tuple的形式存入一个变量，button = (By.CSS_SELECTOR, "XXX")
    def find_element(self, locator):
        # find_element中是两个参数，因此不能直接传locator，而是应该取出locator中的两个值作为参数， 这里用到传多个参数的方式*args
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_element_display(self, locator):
        isVisiable = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*locator))
        assert isVisiable, "The element on locator {} does not display on UI".format(locator)
        return isVisiable

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def get_text(self, locator, text):
        return self.find_element(locator).text

    def get_element_attribute(self, locator, attribute_type):
        return self.find_element(locator).get_attribute(attribute_type)

    def close_browser(self):
        self.driver.close()
