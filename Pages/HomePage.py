import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage


class HomePage(BasePage):
    url = 'https://www.amazon.com'
    title = 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'

    department_dropdown_loc = (By.CSS_SELECTOR, "select[class='nav-search-dropdown searchSelect']")
    search_input_box_loc = (By.CSS_SELECTOR, ".nav-search-field>input")
    search_button_loc = (By.CSS_SELECTOR, "input[type='submit'][class='nav-input']")

    def go_to_home_page(self):
        self.driver.get(self.url)

    def select_department(self, department_name):
        departments = Select(self.find_element(self.department_dropdown_loc))
        departments.select_by_visible_text(department_name)

    def input_search_content(self, search_text):
        self.input_text(self.search_input_box_loc, search_text)

    def click_search_button(self):
        self.click(self.search_button_loc)

    def verify_title(self):
        current_title = self.driver.title
        expected_title = self.title
        assert current_title == expected_title, f"Current title is '{current_title}', it should be '{expected_title}'"
