import requests

BASE_URL = "http://localhost:5000/api/v1"

def test_admin_approve_restaurant():
    response = requests.put(
        f"{BASE_URL}/admin/restaurants/1/approve"
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
