import tests_suite

@tests_suite.mark.smoke
def test_smoke():
    assert True

@tests_suite.fixture()
def setup_teardown():
    print("setup")
    yield
    print("teardown")

def test_example1(setup_teardown):
    print("test1 running")

def test_example2(setup_teardown):
    print("test2 running")