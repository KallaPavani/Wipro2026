from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    cart_link = (By.CLASS_NAME, "ico-cart")
    qty_box = (By.CLASS_NAME, "qty-input")
    update_cart = (By.NAME, "updatecart")
    remove_checkbox = (By.NAME, "removefromcart")
    logout_link = (By.CLASS_NAME, "ico-logout")

    def open_cart(self):
        self.click(self.cart_link)

    def update_quantity(self):
        qty = self.driver.find_element(*self.qty_box)
        qty.clear()
        qty.send_keys("2")
        self.click(self.update_cart)

    def remove_item(self):
        self.click(self.remove_checkbox)
        self.click(self.update_cart)

    def logout(self):
        self.click(self.logout_link)