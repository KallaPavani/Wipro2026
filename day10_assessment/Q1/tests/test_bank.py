import pytest
from day10_assessment.bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)  # initial balance 100

def test_deposit(account):
    assert account.deposit(50) == 150

def test_withdraw(account):
    assert account.withdraw(40) == 60

def test_get_balance(account):
    assert account.get_balance() == 100

def test_deposit_negative(account):
    with pytest.raises(ValueError):
        account.deposit(-20)

def test_withdraw_insufficient(account):
    with pytest.raises(ValueError):
        account.withdraw(200)
