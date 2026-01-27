import pytest

# Module-level setup/teardown
def setup_module(module):
    print("\n--- Setup Module ---")

def teardown_module(module):
    print("\n--- Teardown Module ---")

# Function-level setup/teardown
def setup_function(function):
    print(f"\nSetup for {function.__name__}")

def teardown_function(function):
    print(f"Teardown for {function.__name__}")

# Tests using function-scoped fixture
def test_deposit(account_function):
    assert account_function.deposit(50) == 150

def test_withdraw(account_function):
    assert account_function.withdraw(40) == 60

def test_get_balance(account_function):
    assert account_function.get_balance() == 100

def test_deposit_negative(account_function):
    with pytest.raises(ValueError):
        account_function.deposit(-20)

def test_withdraw_insufficient(account_function):
    with pytest.raises(ValueError):
        account_function.withdraw(200)
