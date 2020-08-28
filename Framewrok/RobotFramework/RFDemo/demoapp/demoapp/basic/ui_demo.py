from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('http://localhost:7272/')
assert 'Login Page' in browser.title

user_name_elem = browser.find_element_by_id('username_field')
password_elem = browser.find_element_by_id('password_field')
login_button_elem = browser.find_element_by_id('login_button')

user_name_elem.send_keys('demo')
password_elem.send_keys('mode')
login_button_elem.click()

assert 'Welcome Page' in browser.title


browser.quit()