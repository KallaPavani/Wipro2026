from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
driver.get("https://www.google.com/")
print("title is", driver.title)
time.sleep(5)
driver.back()
print("title after back:", driver.title)
driver.forward()
print("title after forward:", driver.title)
