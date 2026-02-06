from selenium import webdriver
from selenium.webdriver.common.by import By
class loginpage_PageFactory:
    def __init__(self,driver):
        self.driver = driver
    @property
    def username(self):
        return self.driver.find_element(By.NAME,"username")
    @property
    def password(self):
        return self.driver.find_element(By.NAME,"password")
    @property
    def login_btn(self):
        return self.driver.find_element(By.XPATH,"//button[@type='submit']")

    #username=(By.NAME,"username")
    #password=(By.NAME,"password")
    #login_btn=((By.XPATH,"//button[@type='submit']")

    def enter_username(self,username):
        self.username.send_keys(username)

    def enter_password(self,password):
        self.password.send_keys(password)

    def click_login(self):
        self.login_btn.click()
