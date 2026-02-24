from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductPage(BasePage):

    product_link = (By.CLASS_NAME, "product-title")
    add_to_cart = (By.CSS_SELECTOR, "input[value='Add to cart']")

    def open_first_product(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//h2[@class='product-title']/a)[1]"))
        ).click()

        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-details-page"))
        )

    def add_product_to_cart(self):
        self.click(self.add_to_cart)

        self.handle_alert_if_present()

        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success"))
        )

        self.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success"))
        )