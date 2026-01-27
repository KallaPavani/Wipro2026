import pytest
from day10_assessment.bank import BankAccount


@pytest.fixture
def account_function():
    return BankAccount(100)


@pytest.fixture(scope="module")
def account_module():
    return BankAccount(500)
