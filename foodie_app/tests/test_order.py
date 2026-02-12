import requests

BASE_URL = "http://localhost:5000/api/v1"

def test_place_order():
    response = requests.post(
        f"{BASE_URL}/orders",
        json={
            "user_id": 1,
            "restaurant_id": 1,
            "dish_ids": [1]
        }
    )
    assert response.status_code == 201
    assert response.json()["status"] == "Placed"


def test_place_order_invalid_user():
    response = requests.post(
        f"{BASE_URL}/orders",
        json={
            "user_id": 999,
            "restaurant_id": 1,
            "dish_ids": [1]
        }
    )
    assert response.status_code == 404


def test_view_orders_by_user():
    response = requests.get(
        f"{BASE_URL}/users/1/orders"
    )
    assert response.status_code in [200, 404]


def test_view_orders_by_restaurant():
    response = requests.get(
        f"{BASE_URL}/restaurants/1/orders"
    )
    assert response.status_code in [200, 404]
