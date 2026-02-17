from utilities.read_json import read_test_data
from pages.login_page import LoginPage
import configparser
import time

def test_user_login(setup):

    driver = setup
    config = configparser.ConfigParser()
    config.read("tricentis_project/config/config.ini")
    driver.get(config["DEFAULT"]["base_url"])
    driver.maximize_window()
    driver.implicitly_wait(5)

    data = read_test_data()
    login_data = data["login"]

    login = LoginPage(driver)

    login.login(
        login_data["email"],
        login_data["password"]

    )

    assert login.is_logged_in()
