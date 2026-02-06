from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

from day18_class_work.Loginpage_PageFactory import loginpage_PageFactory

driver=webdriver.Chrome()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
time.sleep(5)
loginobj=loginpage_PageFactory(driver)

loginobj.enter_password("Admin")
loginobj.enter_password("admin123")
loginobj.click_login()


