from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID,"prompt").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
driver.quit()