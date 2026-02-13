import requests

BASE_URL = "http://localhost:5000/api/v1"

def test_place_order():
    # Create restaurant
    r = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": "Test Hotel"}
    )
    restaurant_id = r.json()["id"]

    # Create user
    u = requests.post(
        f"{BASE_URL}/users",
        json={"name": "Pavani"}
    )
    user_id = u.json()["id"]

    # Create dish
    d = requests.post(
        f"{BASE_URL}/dishes",
        json={
            "name": "Biryani",
            "restaurant_id": restaurant_id,
            "price": 200
        }
    )
    dish_id = d.json()["id"]

    # Now place order
    response = requests.post(
        f"{BASE_URL}/orders",
        json={
            "user_id": user_id,
            "restaurant_id": restaurant_id,
            "dish_ids": [dish_id]
        }
    )

    assert response.status_code == 201


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
