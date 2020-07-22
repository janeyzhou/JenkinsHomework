from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Header:
    department_dropdown_loc = (By.CSS_SELECTOR, "select[class='nav-search-dropdown searchSelect']")
    search_input_box_loc = (By.CSS_SELECTOR, ".nav-search-field>input")
    search_button_loc = (By.CSS_SELECTOR, "input[type='submit'][class='nav-input']")

    def select_department(self, department_name):
        departments = Select(self.find_element(self.department_dropdown_loc))
        departments.select_by_visible_text(department_name)

    def input_search_content(self, search_text):
        self.input_text(self.search_input_box_loc, search_text)

    def click_search_button(self):
        self.click(self.search_button_loc)