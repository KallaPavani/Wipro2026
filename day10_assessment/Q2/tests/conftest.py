import tests_suite
from day10_assessment.Q2.bank import BankAccount


@tests_suite.fixture(scope="module")
def account_module():
    print("\n[account_module fixture] Creating BankAccount instance")
    return BankAccount(500)


@tests_suite.fixture(scope="function")
def account_function():
    print("\n[account_function fixture] Creating BankAccount instance")
    return BankAccount(100)
