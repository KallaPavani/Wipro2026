from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    product_link = (By.CLASS_NAME, "product-title")
    add_to_cart = (By.CSS_SELECTOR, "input[value='Add to cart']")

    def open_first_product(self):
        self.driver.find_element(*self.product_link)[0].click()

    def add_product_to_cart(self):
        self.click(self.add_to_cart)