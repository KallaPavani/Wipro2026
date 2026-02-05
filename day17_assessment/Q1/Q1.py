from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#Fill text box
driver.find_element(By.ID,"name").send_keys("Pavani")
time.sleep(2)
driver.find_element(By.ID,"email").send_keys("pavs@test.com")
time.sleep(2)
driver.find_element(By.ID,"phone").send_keys("9876543210")
time.sleep(2)
driver.find_element(By.ID,"textarea").send_keys("Vizag")
time.sleep(2)

#Radio button (Gender)
driver.find_element(By.ID,"female").click()
time.sleep(2)

#CheckBox (days)
driver.find_element(By.ID,"thursday").click()
time.sleep(2)

#Dropdown (Country)
country=Select(driver.find_element(By.ID,"country"))
country.select_by_visible_text("India")
time.sleep(2)

#Date
driver.find_element(By.ID,"datepicker").send_keys("05/02/2026")
time.sleep(2)

#submit
btn = driver.find_element(By.ID, "btn1")
driver.execute_script("arguments[0].scrollIntoView();", btn)
btn.click()

print("Form filled successfully")

time.sleep(2)
driver.quit()
