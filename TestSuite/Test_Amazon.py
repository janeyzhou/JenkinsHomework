import logging
import os

import pytest

from Pages.HomePage import HomePage
from Pages.SearchResultPage import SearchResultPage
from Util.Common import readCSV
from Util.Logger import logger
from Work_Flow.SearchFlow import SearchFlow


class TestSearchDevice:
    test_data = readCSV(os.path.join(os.path.dirname(__file__), '..', 'Test_Data/search_case.csv'))
    @pytest.mark.parametrize("data", test_data)
    def test_search_amazon(self, data, driver):
        logger.info("start")
        home_page = HomePage(driver=driver)
        home_page.go_to_home_page()
        home_page.verify_title()

        search_flow = SearchFlow(driver=driver)
        search_flow.search(data["department"], data["search_text"])

        search_result = SearchResultPage(driver=driver)
        search_result.verify_title(data["search_text"])
        search_result.verify_product_name(data["search_text"])

        search_flow.show_search_result()
