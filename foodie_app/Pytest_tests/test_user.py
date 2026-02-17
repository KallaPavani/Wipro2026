import requests

BASE_URL = "http://localhost:5000/api/v1"

def test_register_user():
    response = requests.post(
        f"{BASE_URL}/users",
        json={
            "name": "Pavani",
            "email": "pavani@test.com"
        }
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Pavani"


def test_register_user_invalid():
    response = requests.post(
        f"{BASE_URL}/users",
        json={}
    )
    assert response.status_code == 400


def test_search_restaurants():
    response = requests.get(
        f"{BASE_URL}/restaurants/search?name=Test"
    )
    assert response.status_code == 200
