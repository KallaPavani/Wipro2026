from utilities.read_json import read_test_data
from pages.register_page import RegisterPage
import configparser

def test_user_registration(setup):

    driver =  setup
    config = configparser.ConfigParser()
    config.read('tricentis_project/config/config.ini')
    driver.get("https://demowebshop.tricentis.com/")

    driver.maximize_window()

    data = read_test_data()
    reg_data = data["registration"]

    register = RegisterPage(driver)

    email = register.register_user(
        reg_data["first_name"],
        reg_data["last_name"],
        reg_data["password"]
    )

    assert "completed" in register.get_success_message()
