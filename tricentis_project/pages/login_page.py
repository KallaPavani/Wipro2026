from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import time

class LoginPage(BasePage):

    login_link = (By.CLASS_NAME, "ico-login")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    login_btn = (By.CSS_SELECTOR, "input.button-1.login-button")
    logout_link = (By.CLASS_NAME, "ico-logout")

    def login(self, email, pwd):
        self.click(self.login_link)
        # wait until the email field is visible
        self.wait.until(EC.visibility_of_element_located(self.email))
        self.enter_text(self.email, email)
        time.sleep(2)
        self.enter_text(self.password, pwd)
        time.sleep(2)
        self.click(self.login_btn)
        time.sleep(3)

    def is_logged_in(self, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(self.logout_link))
            return True
        except TimeoutException:
            return False


