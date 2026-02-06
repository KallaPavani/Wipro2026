from selenium import webdriver
from selenium.webdriver.common.by import By
from day18_assessment.Q1.pages.base_page import BasePage
base_url = "https://tutorialsninja.com/demo/"

class HomePage(BasePage):


    DESKTOPS = (By.LINK_TEXT, "Desktops")
    MAC = (By.LINK_TEXT, "Mac (1)")
    MAC_HEADING = (By.CSS_SELECTOR, "h2")
    SORT = (By.ID, "input-sort")
    ADD_TO_CART = (By.CSS_SELECTOR, ".button-group > button:nth-child(1)")
    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BTN = (By.CSS_SELECTOR, ".btn-default")

    def open_desktops(self):
        self.click(self.DESKTOPS)

    def open_mac(self):
        self.click(self.MAC)

    def get_mac_heading(self):
        return self.get_text(self.MAC_HEADING)

    def sort_by_name_az(self):
        self.select_by_text(self.SORT, "Name (A - Z)")

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART)

    def search_product(self, product):
        self.enter_text(self.SEARCH_BOX, product)
        self.click(self.SEARCH_BTN)
