from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
gap = 3

try:
    driver.get("https://letcode.in/alert")
    # --- 1. Simple Alert ---
    simple_btn = wait.until(EC.element_to_be_clickable((By.ID, "accept")))
    driver.execute_script("arguments[0].click();", simple_btn)

    alert = wait.until(EC.alert_is_present())
    print(f"Simple Alert: {alert.text}")

    time.sleep(gap)
    alert.accept()
    time.sleep(1)

    # --- 2. Confirmation Alert ---
    confirm_btn = wait.until(EC.element_to_be_clickable((By.ID, "confirm")))
    driver.execute_script("arguments[0].click();", confirm_btn)

    alert = wait.until(EC.alert_is_present())
    print(f"Confirm Alert: {alert.text}")

    time.sleep(gap)
    alert.dismiss()
    print("Confirmation dismissed.")
    time.sleep(1)

    # --- 3. Prompt Alert ---
    prompt_btn = wait.until(EC.element_to_be_clickable((By.ID, "prompt")))
    driver.execute_script("arguments[0].click();", prompt_btn)

    alert = wait.until(EC.alert_is_present())
    alert.send_keys("Pavani Kalla")

    time.sleep(gap)
    alert.accept()

    prompt_res = wait.until(EC.presence_of_element_located((By.ID, "myName")))
    print(f"Prompt Result: {prompt_res.text}")
    time.sleep(gap)

finally:
    driver.quit()