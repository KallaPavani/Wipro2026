from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SearchPage(BasePage):

    search_box = (By.ID, "small-searchterms")
    search_btn = (By.CSS_SELECTOR, "input.search-box-button")
    result_item = (By.CSS_SELECTOR, ".product-item")

    def search_product(self, item):
        search_element = self.wait.until(
            EC.visibility_of_element_located(self.search_box)
        )

        search_element.clear()
        search_element.send_keys(item)
        search_element.send_keys(Keys.ENTER)

        # Wait for search results page to load
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "search-results"))
        )

    def search_product(self, item):
        search_element = self.wait.until(
            EC.visibility_of_element_located(self.search_box)
        )

        search_element.clear()
        search_element.send_keys(item)
        search_element.send_keys(Keys.ENTER)

        # Wait for search results page to load
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "search-results"))
        )

    def results_found(self):
        try:
            # Wait up to 5 seconds for at least one product box to appear
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-item")))
            return True
        except:
            return False