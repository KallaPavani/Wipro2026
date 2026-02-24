import pytest
import logging
from selenium import webdriver
from datetime import datetime
import configparser
import os


# ==============================
# Read config.ini
# ==============================

config = configparser.ConfigParser()

config_path = os.path.join(
    os.path.dirname(__file__),
    "config",
    "config.ini"
)

config.read(config_path)

browser_from_config = config["DEFAULT"]["browser"]
base_url_from_config = config["DEFAULT"]["base_url"]


# ==============================
# Driver Fixture(For Not secure error)
# ==============================

@pytest.fixture
def driver():

    browser = browser_from_config.lower()
    logging.info(f"Launching browser: {browser}")

    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--allow-insecure-localhost")

        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options

        firefox_options = Options()
        firefox_options.set_preference("dom.webnotifications.enabled", False)
        firefox_options.accept_insecure_certs = True

        driver = webdriver.Firefox(options=firefox_options)

    elif browser == "edge":
        from selenium.webdriver.edge.options import Options

        edge_options = Options()
        edge_options.add_argument("--ignore-certificate-errors")
        edge_options.add_argument("--allow-insecure-localhost")

        driver = webdriver.Edge(options=edge_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


# ==============================
# Base URL Fixture
# ==============================

@pytest.fixture
def base_url():
    return base_url_from_config


# ==============================
# Screenshot on Failure Hook
# ==============================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = os.path.join("tests_suite", "tests", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = os.path.join(
                screenshots_dir,
                f"failure_{timestamp}.png"
            )

            driver.save_screenshot(file_name)
            logging.error(f"Screenshot saved: {file_name}")