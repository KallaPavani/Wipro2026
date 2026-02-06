from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def select_by_text(self, locator, text):
        Select(self.driver.find_element(*locator)).select_by_visible_text(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text
