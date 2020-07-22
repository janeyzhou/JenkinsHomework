import logging

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Util.Logger import logger


class SearchResultPage(BasePage):

    title_loc = (By.CSS_SELECTOR, "div[data-component-type='s-search-result'] span[class='a-size-medium a-color-base a-text-normal']")
    price_loc = (By.CSS_SELECTOR, "div[data-component-type='s-search-result'] span[class='a-price']>span[class='a-offscreen']")

    def verify_title(self, search_text):
        current_title = self.driver.title
        expected_tittle = f"Amazon.com : {search_text}"
        assert current_title == expected_tittle, f"Current title is '{current_title}', it should be '{expected_tittle}'"

    def get_product_name(self):
        name_elements = self.find_elements(self.title_loc)
        name_list = []
        if len(name_elements) == 0:
            logging.info('Did not find any products')
        else:
            for element in name_elements:
                name_list.append(element.text)
        return name_list

    def get_product_price(self):
        price_elements = self.find_elements(self.price_loc)
        price_list = []
        if len(price_elements) == 0:
            logger.info('Did not find any products')
        else:
            for element in price_elements:
                price_list.append(element.text)
        return price_list

    def verify_product_name(self, search_text):
        names = self.get_product_name()
        for name in names:
            assert search_text in name, f"'{search_text}' is not in product name '{name}'"



