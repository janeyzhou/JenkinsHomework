from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from DPAuto.PageFactory.BasePage import BasePage



class HomePage(BasePage):

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



