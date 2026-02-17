from utilities.read_json import read_test_data
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import configparser

def tet_logout_and_session_validation(setup):

    driver = setup
    config = configparser.ConfigParser()
    config.read("tricentis_project/config/config.ini")
    driver.get(config["DEFAULT"]["base_url"])

    data = read_test_data()

    #Login
    login = LoginPage(driver)
    login.login(
        data["login"]["email"],
        data["login"]["password"]
    )

    #Logout
    cart = CartPage(driver)
    cart.logout()

    assert "Log in" in driver.page_source