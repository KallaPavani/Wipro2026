from day18_assessment.Q1.pages.home_page import HomePage
from day18_assessment.Q1.pages.home_page import base_url

def test_mac_product_flow(driver):
    driver.get(base_url)
    home = HomePage(driver)

    home.open_desktops()
    home.open_mac()

    assert home.get_mac_heading() == "Mac"

    home.sort_by_name_az()
    home.add_product_to_cart()
    home.search_product("Monitors")

    print("Test Passed Successfully")

