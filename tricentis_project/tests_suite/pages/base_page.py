from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def handle_alert_if_present(self):
        try:
            alert = self.driver.switch_to.alert
            print(f"Alert found: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            pass