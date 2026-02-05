from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID,"modern").click()
text=driver.find_element(By.CLASS_NAME,"modal").click()
print("Modern Alert:" ,text)
time.sleep(2)
driver.quit()