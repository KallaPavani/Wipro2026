from utilities.read_json import read_test_data
from pages.search_page import SearchPage
import configparser

def test_product_search(setup):

    driver = setup
    config =  configparser.ConfigParser()
    config.read('tricentis_project/config/config.ini')
    driver.get(config["DEFAULT"]["base_url"])
    driver.maximize_window()

    data = read_test_data()

    search = SearchPage(driver)

    search.search_product(data["search"]["product"])

    assert search.results_found()
