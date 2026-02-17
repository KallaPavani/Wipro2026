import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/api/v1"

@pytest.fixture(autouse=True)
def reset_app():
    requests.post(f"{BASE_URL}/reset")
