from selenium.webdriver.common.by import By

class Lab_11_Locators:

    desktops_link = (By.LINK_TEXT, "Desktops")
    mac_link = (By.LINK_TEXT, "Mac (1)")
    mac_heading = (By.CSS_SELECTOR, "h2")

    sort_dropdown = (By.ID, "input-sort")
    sort_name_AZ = (By.XPATH, "//option[text()='Name (A - Z)']")

    add_to_cart = (By.CSS_SELECTOR, ".button-group > button:nth-child(1)")

    search_box = (By.NAME, "search")
    search_button = (By.CSS_SELECTOR, ".btn-default")

    description_checkbox = (By.ID, "description")
    search_submit = (By.ID, "button-search")
