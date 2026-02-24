from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):

    cart_link = (By.CLASS_NAME, "ico-cart")
    qty_box = (By.CLASS_NAME, "qty-input")
    update_cart = (By.NAME, "updatecart")
    remove_checkbox = (By.NAME, "removefromcart")
    logout_link = (By.CLASS_NAME, "ico-logout")
    empty_cart_message = (By.CSS_SELECTOR, ".order-summary-content")

    def open_cart(self):
        self.click(self.cart_link)

    def update_quantity(self, quantity):
        qty = self.wait.until(EC.visibility_of_element_located(self.qty_box))
        qty.clear()
        qty.send_keys(quantity)
        self.click(self.update_cart)

    def remove_item(self):
        self.click(self.remove_checkbox)
        self.click(self.update_cart)

    def get_empty_cart_message(self):
        # This waits for the element to be visible/present again after the refresh
        element = self.wait.until(EC.visibility_of_element_located(self.empty_cart_message))
        return element.text