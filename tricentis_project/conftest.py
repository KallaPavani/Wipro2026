import pytest
from utilities.driver_factory import get_driver
import os

@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs['setup']
        os.makedirs("Screenshots of POSTMAN", exist_ok=True)
        driver.save_screenshot(f"Screenshots of POSTMAN/{item.name}.png")
