import tests_suite
from day10_assessment.bank import BankAccount


@tests_suite.fixture
def account_function():
    return BankAccount(100)


@tests_suite.fixture(scope="module")
def account_module():
    return BankAccount(500)
