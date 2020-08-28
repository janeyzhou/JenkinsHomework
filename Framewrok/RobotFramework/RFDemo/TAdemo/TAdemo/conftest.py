from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome()  # if not added in PATH
    driver.get("http://localhost:7272")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()