from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import time

class RegisterPage(BasePage):

    register_link = (By.CLASS_NAME, "ico-register")

    gender_male = (By.ID, "gender-male")
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    confirm_password = (By.ID, "ConfirmPassword")
    register_button = (By.ID, "register-button")
    success_message = (By.CLASS_NAME, "result")

    def register_user(self, fname, lname, pwd):

        self.click(self.register_link)

        unique_email = f"test{random.randint(1000,9999)}@mail.com"

        self.click(self.gender_male)
        self.enter_text(self.first_name, fname)
        time.sleep(1)
        self.enter_text(self.last_name, lname)
        time.sleep(1)
        self.enter_text(self.email, unique_email)
        time.sleep(1)
        self.enter_text(self.password, pwd)
        time.sleep(1)
        self.enter_text(self.confirm_password, pwd)
        time.sleep(1)
        self.click(self.register_button)
        time.sleep(3)

        return unique_email

    def get_success_message(self):
        return self.get_text(self.success_message)
