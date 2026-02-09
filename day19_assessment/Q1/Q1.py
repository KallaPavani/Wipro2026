from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1. Implicit Wait
driver.implicitly_wait(10)
driver.get("https://tutorialsninja.com/demo/")

# 2. Explicit Wait – Search box
try:
    wait = WebDriverWait(driver, 15)

    search_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "search"))
    )
    search_input.send_keys("MacBook")
    print("Explicit Wait: Search box is clickable.")

    search_input.send_keys(Keys.ENTER)

except TimeoutException:
    print("Explicit wait failed: Search box not found.")
    driver.quit()
    exit()

# 3. Fluent Wait – Wait for product results
try:
    fluent_wait = WebDriverWait(
        driver,
        timeout=20,
        poll_frequency=2,
        ignored_exceptions=[NoSuchElementException]
    )

    first_product = fluent_wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.product-layout")
        )
    )

    print("Fluent Wait: Product results loaded successfully.")

except TimeoutException:
    print("Fluent wait failed: Products did not load.")

time.sleep(3)
driver.quit()
