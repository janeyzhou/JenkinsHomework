import logging

from Pages.HomePage import HomePage
from Pages.SearchResultPage import SearchResultPage
from Util.Logger import logger


class SearchFlow:
    def __init__(self, driver):
        self.home_page = HomePage(driver)
        self.search_result_page = SearchResultPage(driver)

    def search(self, department, search_text):
        self.home_page.select_department(department)
        self.home_page.input_search_content(search_text)
        self.home_page.click_search_button()

    def show_search_result(self):
        name = self.search_result_page.get_product_name()
        price = self.search_result_page.get_product_price()
        for i in range(len(name)-1):
            logger.info(f"{name[i]}: {price[i]}")