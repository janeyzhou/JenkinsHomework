from selenium import webdriver


class Singleton(object):

    instance = None

    def __new__(cls, base_url, browser='chrome'):

        if cls.instance is None:
            i = object.__new__(cls)
            cls.instance = i
            cls.base_url = base_url
            cls.browser = browser

            if browser == "firefox":
                # Create a new instance of the Firefox driver
                cls.driver = webdriver.Firefox()
            elif browser == "chrome":
                cls.driver = webdriver.Chrome()
            elif browser == "remote":
                # Create a new instance of the Chrome driver
                cls.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)
            else:
                # Sorry, we can't help you right now.
                print("Support for Firefox or Remote only!")

        else:

            i = cls.instance

        return i


if __name__ == '__main__':
    test_a = Singleton('https://www.google.com/')
    print(test_a.instance)
    print(test_a.driver)
    print(test_a.browser)

    test_b = Singleton('https://www.baidu.com/')
    print(test_b.instance)
    print(test_b.driver)
    print(test_b.browser)