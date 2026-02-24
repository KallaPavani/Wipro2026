import pytest  # You must import pytest itself
import logging
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from data.load_users import load_test_data

@pytest.mark.parametrize("data", load_test_data()) # Fixed: Use pytest.mark, not tests_suite.mark
def test_complete_flow(driver, data, base_url):
    logging.info("--- Starting E2E Flow Test ---")

    # Initialize Pages
    register = RegisterPage(driver)
    login = LoginPage(driver)
    home = HomePage(driver)
    search = SearchPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    # Step 1: Navigation
    logging.info(f"Step 1: Navigating to base URL: {base_url}")
    driver.get(base_url)
    driver.maximize_window()
    logging.info("Window maximized and home page loaded.")

    # Step 2: Registration
    logging.info(f"Step 2: Starting registration for {data['firstname']} {data['lastname']}.")
    generated_email = register.register_user(
        gender=data["gender"],
        fname=data["firstname"],
        lname=data["lastname"],
        email=data["email"],
      password=data["password"],
        confirm_password=data["confirm_password"],
    )
    logging.info(f"User registration submitted with email: {generated_email}")

    success_msg = register.get_success_message().lower()
    logging.info(f"Registration message received: '{success_msg}'")
    assert "your registration completed" in success_msg

    logging.info("Logging out post-registration.")
    home.click_logout()

    # Step 3: Login
    logging.info(f"Step 3: Attempting login with {generated_email}")
    login.login(generated_email, data["password"])

    is_logged_in = login.is_logged_in()
    logging.info(f"Login success status: {is_logged_in}")
    assert is_logged_in

    # Step 4: Search and add product
    logging.info(f"Step 4: Searching for item: {data['search_item']}")
    search.search_product(data["search_item"])

    res_found = search.results_found()
    logging.info(f"Search results found: {res_found}")
    assert res_found

    logging.info("Opening product details and adding to cart.")
    product.open_first_product()
    product.add_product_to_cart()
    logging.info("Product successfully added to cart.")

    # Step 5: Cart update and remove
    logging.info("Step 5: Opening cart to manage items.")
    cart.open_cart()

    qty = data["quantity"]
    logging.info(f"Updating item quantity to: {qty}")
    cart.update_quantity(qty)

    logging.info("Removing item from cart for cleanup.")
    cart.remove_item()

    empty_msg = cart.get_empty_cart_message().lower()
    logging.info(f"Cart status message: '{empty_msg}'")
    assert "empty" in empty_msg

    # Step 6: Logout
    logging.info("Step 6: Logging out of the application.")
    home.click_logout()

    logged_out = home.is_logged_out()
    logging.info(f"Logout confirmation: {logged_out}")
    assert logged_out

    logging.info("--- E2E Flow Test Passed Successfully ---")

#pytest test_E2E.py --browser=edge --html=reports/edge_report.html --self-contained-html
#pytest test_E2E.py --browser=chrome --html=reports/chrome_report.html --self-contained-html
#pytest test_E2E.py --browser=firefox --html=reports/firefox_report.html --self-contained-html