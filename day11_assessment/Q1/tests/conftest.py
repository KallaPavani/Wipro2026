import tests_suite

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run Pytest_tests against"
    )

@tests_suite.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")
