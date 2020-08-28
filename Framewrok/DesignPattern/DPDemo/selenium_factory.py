import selenium.webdriver as webdriver
from proboscis import TestProgram
from proboscis import test
from proboscis import before_class
from proboscis import after_class


class WebdriverFactory:
    @staticmethod
    def getWebdriver(browserName):
        if (browserName == 'firefox'):
            return webdriver.Firefox()
        elif (browserName == 'chrome'):
            return webdriver.Chrome()
        elif (browserName == 'ie'):
            return webdriver.Ie()

        raise Exception("No such " + browserName + " browser exists")


class Page_Object:
    def __init__(self, driver):
        self.driver = driver

    def go_to_home(self):
        self.driver.get("http://google.com")
        return self

    def go_to_page(self, url):
        self.driver.get(url)
        return self

    def run_search(self, url, query):
        self.driver.get(url)
        self.driver.find_element_by_id(locators['search_box']).send_keys(query)
        self.driver.find_element_by_id(locators['search_button']).click()

    def tear_down(self):
        self.driver.close()


@test(groups=['selenium'])
class Test_Scripts:

    @test(groups=['WebDemo'])
    def test_1(self):
        driver = WebdriverFactory.getWebdriver("firefox")
        pageObj = Page_Object(driver)
        pageObj.run_search("http://google.com", 'apples')
        pageObj.tear_down()

    def run_tests(self):
        TestProgram().run_and_exit()


Test_Scripts().run_tests()