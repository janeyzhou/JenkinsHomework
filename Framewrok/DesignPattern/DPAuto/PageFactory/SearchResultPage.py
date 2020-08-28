from selenium.webdriver.common.by import By

from DPAuto.PageFactory.BasePage import BasePage


class SearchResultPage(BasePage):

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


