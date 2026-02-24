from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random


class RegisterPage(BasePage):

    register_link = (By.CLASS_NAME, "ico-register")

    gender_male = (By.ID, "gender-male")
    gender_female = (By.ID, "gender-female")
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    confirm_password = (By.ID, "ConfirmPassword")
    register_button = (By.ID, "register-button")
    success_message = (By.CLASS_NAME, "result")

    def register_user(self, fname, lname, email, password, confirm_password,gender):

        self.click(self.register_link)

        if gender.lower() == "male":
            self.click(self.gender_male)
        elif gender.lower() == "female":
            self.click(self.gender_female)

        # Generate unique email properly
        random_number = random.randint(1000, 9999)

        if "@" in email:
            local, domain = email.split("@")
            unique_email = f"{local}{random_number}@{domain}"
        else:
            unique_email = f"{email}{random_number}@testmail.com"

        self.enter_text(self.first_name, fname)
        self.enter_text(self.last_name, lname)
        self.enter_text(self.email, unique_email)
        self.enter_text(self.password, password)
        self.enter_text(self.confirm_password, confirm_password)
        self.click(self.register_button)

        return unique_email

    def get_success_message(self):
        return self.get_text(self.success_message)
