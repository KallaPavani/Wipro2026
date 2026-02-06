from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        username=(By.NAME,"username")
        password=(By.NAME,"password")
        login_btn=(By.XPATH,"//button[atype='submit']")

        def enter_username(self,user):
            self.driver.find_element(*self.username).send_keys(user)

        def enter_password(self,pwd):
            self.driver.find_element(*self.password).send_keys(pwd)

        def click_login(self):
            self.driver.find_element(*self.login_btn).click()