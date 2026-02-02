import requests


def test_booking_success(base_url):
    payload = {"movie_id": 104, "tickets": 4}
    response = requests.post(f"{base_url}/api/bookings", json=payload)
    assert response.status_code == 201

def test_booking_failure(base_url):
    payload = {"movie_id": 105, "tickets": 0}
    response = requests.post(f"{base_url}/api/bookings", json=payload)
    assert response.status_code == 400