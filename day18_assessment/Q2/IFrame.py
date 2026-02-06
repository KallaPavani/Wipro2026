from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#1. Start Browser
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://letcode.in/frame")

#Switch to the first frame by index (0)
driver.switch_to.frame(0)

driver.find_element(By.NAME,"fname").send_keys("Pavani")
driver.find_element(By.NAME, "lname").send_keys("Kalla")

#Switch back to main page
driver.switch_to.default_content()
print("Switched back to main page")


#Opening new tab using JS
driver.execute_script("window.open('https://example.com', '_blank');")
time.sleep(2)

window_handles=driver.window_handles
parent_window=driver.window_handles[0]
child_window=driver.window_handles[1]

#Switch to child window and print title
driver.switch_to.window(child_window)
print("Child window title:", driver.title)

#Switch to parent window and parent title
driver.switch_to.window(parent_window)
print("Parent window title:", driver.title)

#Close child window
driver.switch_to.window(child_window)
driver.close()

#Return to parent window again
driver.switch_to.window(parent_window)
print("Returned to parent:", driver.title)

time.sleep(2)
driver.quit()

