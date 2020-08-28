from DPAuto.Singleton.SingletonPages import *
driver = WebDriverFactory.getWebDriver()
home_page = SingletonHomePage(driver)
home_page.go_to_home_page()
home_page.select_a_search_department("Electronics")
home_page.input_context_to_search_box('kindle')
home_page.click_search_button()
search_result_page = SingletonSearchResultPage(driver)
search_result_page.verify_search_text_display_on_search_result_title("kindle")
search_result_page.get_product_details()

