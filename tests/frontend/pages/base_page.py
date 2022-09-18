from tests.config import BaseConfig

class BasePage:
    def __init__(self, selenium_driver, base_url = BaseConfig.BASE_URL):
        self.base_url = base_url
        self.driver = selenium_driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def basic_auth(self, username, password):
        return self.base_url[:7] + username + ':' + password + '@' + self.base_url[7:]

    def open(self, username = BaseConfig.USERNAME, password = BaseConfig.PASSWORD):
        return self.driver.get(self.basic_auth(username, password))