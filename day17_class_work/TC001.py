from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
title=driver.title
print("title is:",title)
currenturl=driver.current_url
print("url:", currenturl)
pagesource=driver.page_source
print("pagesource:", pagesource)
