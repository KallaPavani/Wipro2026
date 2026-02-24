import tests_suite

@tests_suite.fixture
def base_url():
    return "http://127.0.0.1:5000/"
