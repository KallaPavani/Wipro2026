from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#Selenium Grid URL
GRID_URL="http://localhost:4444/wd/hub"

#Browsers to test
browsers=[
    ("chrome",ChromeOptions()),
    ("firefox",FirefoxOptions()),
]
for browser_name, options in browsers:
    driver=webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    try:
        driver.get("https://google.com")

        #Verify page title
        expected_title="Google"
        actual_title=driver.title

        print("Browser:", driver.capabilities.get("browserName"))
        print("Platform:", driver.capabilities.get("platformName"))

        if actual_title==expected_title:
            print("Title verification PASSED\n")
        else:
            print("Title verification FAILED\n")

    finally:
        driver.quit()