from selenium import webdriver
import pytest
import allure

@pytest.fixture(scope="function")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome()  # if not added in PATH
    driver.get("http://localhost:7272")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    if request.session.testsfailed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")

            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass  # just ignore

        # Close browser window:
    driver.close()