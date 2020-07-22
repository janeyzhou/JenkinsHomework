import logging

import allure
import pytest

from Pages.PageFactory import PageFactory
from Util.Logger import logger


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    logger.info("init driver...")
    driver = PageFactory.getWebDriver(driver="Chrome")

    def fn():
        driver.close()

    request.addfinalizer(fn)
    return driver


@pytest.fixture(scope="function", autouse=True)
def teardown_function(request, driver):
    yield
    if request.session.testsfailed:
        driver.execute_script("document.body.bgColor = 'white';")
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=allure.attachment_type.PNG)
