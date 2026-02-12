import requests
import uuid

BASE_URL = "http://localhost:5000/api/v1"


def create_restaurant():
    unique_name = "Hotel_" + str(uuid.uuid4())

    response = requests.post(
        f"{BASE_URL}/restaurants",
        json={
            "name": unique_name,
            "category": "Indian",
            "location": "Hyderabad",
            "contact": "9999999999"
        }
    )

    assert response.status_code == 201
    return response.json()["id"]


def create_dish(restaurant_id):
    response = requests.post(
        f"{BASE_URL}/restaurants/{restaurant_id}/dishes",
        json={
            "name": "Biryani_" + str(uuid.uuid4()),
            "type": "Main Course",
            "price": 250,
            "available_time": "Lunch"
        }
    )

    assert response.status_code == 201
    return response.json()["id"]


def test_add_dish():
    restaurant_id = create_restaurant()
    dish_id = create_dish(restaurant_id)
    assert dish_id is not None


def test_update_dish():
    restaurant_id = create_restaurant()
    dish_id = create_dish(restaurant_id)

    response = requests.put(
        f"{BASE_URL}/dishes/{dish_id}",
        json={"price": 300}
    )

    assert response.status_code == 200


def test_disable_dish():
    restaurant_id = create_restaurant()
    dish_id = create_dish(restaurant_id)

    response = requests.put(
        f"{BASE_URL}/dishes/{dish_id}/status",
        json={"enabled": False}
    )

    assert response.status_code == 200


def test_delete_dish():
    restaurant_id = create_restaurant()
    dish_id = create_dish(restaurant_id)

    response = requests.delete(f"{BASE_URL}/dishes/{dish_id}")

    assert response.status_code == 200
