from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

url = "https://automationteststore.com/index.php?rt=account/create"
driver.get(url)

# -------- VERIFY PAGE --------
print("Page title is:", driver.title)
time.sleep(1)

# -------- PERSONAL DETAILS --------
driver.find_element(By.ID, "AccountFrm_firstname").send_keys("Pavani")
time.sleep(1)

driver.find_element(By.ID, "AccountFrm_lastname").send_keys("Kalla")
time.sleep(1)

driver.find_element(By.ID, "AccountFrm_email").send_keys(f"pavani{int(time.time())}@test.com")
time.sleep(1)

driver.find_element(By.ID, "AccountFrm_telephone").send_keys("9876543210")
time.sleep(1)

# -------- ADDRESS DETAILS --------
driver.find_element(By.ID, "AccountFrm_company").send_keys("Conduent")
time.sleep(1)

driver.find_element(By.ID, "AccountFrm_address_1").send_keys("123 Main Street")
time.sleep(1)

driver.find_element(By.ID, "AccountFrm_address_2").send_keys("Near Park")
time.sleep(1)

driver.find_element(By.ID, "AccountFrm_city").send_keys("Hyderabad")
time.sleep(1)

driver.find_element(By.ID, "AccountFrm_postcode").send_keys("500001")
time.sleep(1)

# Country dropdown
country = Select(driver.find_element(By.ID, "AccountFrm_country_id"))
country.select_by_visible_text("India")
time.sleep(2)

# State dropdown
state = Select(driver.find_element(By.ID, "AccountFrm_zone_id"))
state.select_by_index(1)
time.sleep(1)

# -------- LOGIN DETAILS --------
driver.find_element(By.ID, "AccountFrm_loginname").send_keys(f"user{int(time.time())}")
time.sleep(1)

driver.find_element(By.ID, "AccountFrm_password").send_keys("Test@1234")
time.sleep(1)

driver.find_element(By.ID, "AccountFrm_confirm").send_keys("Test@1234")
time.sleep(1)

# -------- NEWSLETTER --------
driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()
time.sleep(1)

# -------- PRIVACY POLICY --------
driver.find_element(By.NAME, "agree").click()
time.sleep(1)

# -------- SUBMIT --------
driver.find_element(By.XPATH, "//button[@title='Continue']").click()

# -------- VERIFY SUCCESS --------
success_msg = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".maintext"))
).text

print("Success message:", success_msg)
assert "your account has been created" in success_msg.lower()
print("Account created successfully")

time.sleep(3)
driver.quit()
