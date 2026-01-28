import pytest
from ..auth import login


def test_valid_login():
    assert login("admin", "Welcome123") == "Login Successful"

def test_invalid_login():
    assert login("user", "Strong456") == "Login Unsuccessful, Invalid Credentials"