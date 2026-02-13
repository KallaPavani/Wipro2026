import requests

BASE_URL = "http://localhost:5000/api/v1"

def test_admin_approve_restaurant():
    # Step 1: Create restaurant
    create = requests.post(
        f"{BASE_URL}/restaurants",
        json={"name": "Test Hotel"}
    )

    restaurant_id = create.json()["id"]

    # Step 2: Approve it
    response = requests.put(
        f"{BASE_URL}/admin/restaurants/{restaurant_id}/approve"
    )

    assert response.status_code == 200



def test_admin_view_orders():
    response = requests.get(
        f"{BASE_URL}/admin/orders"
    )
    assert response.status_code == 200


def test_admin_view_ratings():
    response = requests.get(
        f"{BASE_URL}/admin/ratings"
    )
    assert response.status_code == 200
