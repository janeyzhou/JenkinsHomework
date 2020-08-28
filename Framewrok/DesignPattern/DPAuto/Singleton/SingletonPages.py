from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

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


class SingletonBasePage(object):
    instance = None

    def __new__(cls, driver):
        if cls.instance is None:
            i = object.__new__(cls)
            cls.driver = driver

            # if browser == "firefox":
            #     # Create a new instance of the Firefox driver
            #     cls.driver = webdriver.Firefox()
            # elif browser == "Chrome":
            #     cls.driver = webdriver.Chrome()
            # elif browser == "remote":
            #     # Create a new instance of the Chrome driver
            #     cls.driver = webdriver.Remote("http://localhost:4444/wd/hub",
            #                                   webdriver.DesiredCapabilities.HTMLUNITWITHJS)
            # else:
            #     # Sorry, we can't help you right now.
            #     print("Support for Firefox or Remote only!")
        else:
            i = cls.instance
        return i

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_element_display(self, locator, ):
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


class SingletonHomePage(SingletonBasePage):
    url = 'https://www.amazon.com'

    department_dropdown_loc = (By.CSS_SELECTOR, "select[class='nav-search-dropdown searchSelect']")
    search_input_box_loc = (By.CSS_SELECTOR, ".nav-search-field>input")
    search_button_loc = (By.CSS_SELECTOR, "input[type='submit'][class='nav-input']")

    def go_to_home_page(self):
        self.driver.get(self.url)
        page_title = self.get_home_page_title()
        assert page_title.find('Amazon') >= 0, "the home page title '{}' does not contain 'Amazon'".format(page_title)

    def get_home_page_title(self):
        return self.driver.title

    def select_a_search_department(self, department_name):
        department_select = Select(self.find_element(self.department_dropdown_loc))
        department_select.select_by_visible_text(department_name)

    def input_context_to_search_box(self, search_text):
        self.input_text(self.search_input_box_loc, search_text)

    def click_search_button(self):
        self.click(self.search_button_loc)



class SingletonSearchResultPage(SingletonBasePage):

    search_result_list_loc = (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    title_loc = (By.CSS_SELECTOR, "div[data-component-type='s-search-result'] span[class='a-size-medium a-color-base a-text-normal']")
    price_loc = (By.CSS_SELECTOR, "div[data-component-type='s-search-result'] span[class='a-price']>span[class='a-offscreen']")

    # 操作放在方法中，方法尽量细化，主流程中不要太多assert，对于验证的地方另写单独的方法
    def wait_to_display_search_result(self):
        self.wait_element_display(self.search_result_list_loc)

    def get_title_from_search_result_list(self):
        title_list = []
        for title in self.find_elements(self.title_loc):
            title_list.append(title.text)
        return title_list

    def get_price_from_search_result_list(self):
        price_list = []
        for price in self.find_elements(self.price_loc):
            price_list.append(price.get_attribute('innerHTML'))
        return price_list

    def verify_search_text_display_on_search_result_title(self, search_text):
        for title in self.get_title_from_search_result_list():
            assert title.find(search_text), "the search text {} does not display in title {}".format(search_text, title)

    def get_product_details(self):
        titles = self.get_title_from_search_result_list()
        prices = self.get_price_from_search_result_list()
        product_details = zip(titles, prices)
        for product in product_details:
            print("{}: {}".format(product[0], product[1]))







