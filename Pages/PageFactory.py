import os

from selenium import webdriver


class PageFactory:
    @staticmethod
    def getWebDriver(driver='Chrome'):

        if driver == 'Chrome':
            return webdriver.Chrome('C:/driver/chromedriver.exe')
        elif driver == 'Firefox':
            return webdriver.firefox("../Driver/firefoxdriver.exe")
        elif driver == 'remote':
            return webdriver.remote("...")
        else:
            raise Exception("Browser {} does not exist".format(driver))
