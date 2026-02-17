from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class SearchPage(BasePage):

    search_box = (By.ID, "small-searchterms")
    search_btn = (By.CSS_SELECTOR, "input.search-box-button")
    result_item = (By.CSS_SELECTOR, ".product-item")

    def search_product(self, product):
        self.enter_text(self.search_box, product)
        time.sleep(2)
        self.click(self.search_btn)
        time.sleep(2)

    def results_found(self):
        return len(self.driver.find_elements(*self.result_item)) > 0