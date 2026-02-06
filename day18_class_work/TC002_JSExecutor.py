from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(5)
#driver.execute_script("alert('Hello Pavani')")
driver.execute_script("window.scrollBy(0,300)")
time.sleep(2)
#driver.execute_script("(0,document.body.scrollHeight)")
