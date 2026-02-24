import tests_suite
from selenium import webdriver

@tests_suite.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()