from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://letcode.in/frame")

    # 1. Switch to iframe using a locator instead of index (more stable)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "firstFr")))

    # 2. Wait for elements inside the frame
    fname = wait.until(EC.presence_of_element_located((By.NAME, "fname")))
    fname.send_keys("Pavani")
    driver.find_element(By.NAME, "lname").send_keys("Kalla")

    # 3. Switch back
    driver.switch_to.default_content()

    # 4. Open new tab and wait for it to exist
    parent_window = driver.current_window_handle
    driver.execute_script("window.open('https://example.com', '_blank');")

    # Wait until there are 2 windows open
    wait.until(lambda d: len(d.window_handles) == 2)

    all_handles = driver.window_handles
    child_window = [h for h in all_handles if h != parent_window][0]

    driver.switch_to.window(child_window)
    print("Child window title:", driver.title)

    driver.switch_to.window(parent_window)
    print("Parent window title:", driver.title)

    # 6. Clean up
    driver.switch_to.window(child_window)
    driver.close()
    driver.switch_to.window(parent_window)

finally:
    time.sleep(2)
    driver.quit()