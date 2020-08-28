from DPAuto.PageFactory.BasePage import WebDriverFactory
from DPAuto.PageFactory.HomePage import HomePage
from DPAuto.PageFactory.SearchResultPage import SearchResultPage

driver = WebDriverFactory.getWebDriver()

search = {"Electronics": "kindle", "book": "tester"}
home_page = HomePage(driver)
home_page.go_to_home_page()
home_page.select_a_search_department("Electronics")
home_page.input_context_to_search_box("kindle")
home_page.click_search_button()
search_result_page = SearchResultPage(driver)
search_result_page.verify_search_text_display_on_search_result_title("kindle")
search_result_page.get_product_details()