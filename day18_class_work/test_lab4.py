import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLab4:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_lab4(self):
        self.driver.get("https://tutorialsninja.com/demo/")
        self.driver.set_window_size(1296, 688)

        # Verify title
        assert self.driver.title == "Your Store"

        # Desktops → Mac
        self.driver.find_element(By.LINK_TEXT, "Desktops").click()
        self.driver.find_element(By.LINK_TEXT, "Mac (1)").click()

        # Verify Mac heading
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Mac"

        # Sort By Name (A - Z)
        self.driver.find_element(By.ID, "input-sort").click()
        self.driver.find_element(
            By.XPATH, "//option[text()='Name (A - Z)']"
        ).click()

        # Add to Cart
        self.driver.find_element(By.CSS_SELECTOR, ".button-group .fa-shopping-cart").click()

        # Search for Mobile
        search = self.driver.find_element(By.NAME, "search")
        search.clear()
        search.send_keys("Mobile")
        self.driver.find_element(By.CSS_SELECTOR, ".fa-search").click()

        # Clear search criteria
        search = self.driver.find_element(By.NAME, "search")
        search.clear()

        # Search in product descriptions
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "button-search").click()

        time.sleep(2)
