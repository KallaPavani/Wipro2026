from utilities.read_json import read_test_data
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import configparser

def test_cart_operations(setup):

    driver = setup
    config = configparser.ConfigParser()
    config.read("tricentis_project/config/config.ini")
    driver.get(config["DEFAULT"]["base_url"])

    data = read_test_data()

    #Login first
    login = LoginPage(driver)
    login.login(
        data["login"]["email"],
        data["login"]["password"]
    )

    #Search
    search = SearchPage(driver)
    search.search_product(data["search"]["product"])

    #Open product
    product = ProductPage(driver)
    product.open_first_product()
    product.add_product_to_cart()

    # Cart actions
    cart = CartPage(driver)
    cart.open_cart()
    cart.update_quantity()
    cart.remove_item()

    assert "Shopping cart" in driver.title


