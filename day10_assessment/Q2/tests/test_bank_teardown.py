# This file shows that module-scoped fixture can be shared
def test_module_fixture(account_module):
    assert account_module.deposit(100) == 600
    assert account_module.withdraw(50) == 550
