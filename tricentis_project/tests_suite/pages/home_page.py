from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    register_link = (By.CLASS_NAME, "ico-register")
    login_link = (By.CLASS_NAME, "ico-login")
    search_box = (By.ID, "small-searchterms")
    search_button = (By.CSS_SELECTOR, "input.button-1.search-box-button")
    cart_link = (By.CLASS_NAME, "ico-cart")
    logout_link = (By.CLASS_NAME, "ico-logout")

    def click_register(self):
        self.click(self.register_link)

    def click_login(self):
        self.click(self.login_link)

    def search_product(self, product_name):
        self.enter_text(self.search_box, product_name)
        self.click(self.search_button)

    def click_cart(self):
        self.click(self.cart_link)

    def click_logout(self):
        self.click(self.logout_link)

    def is_logged_out(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.register_link)
        ).is_displayed()

