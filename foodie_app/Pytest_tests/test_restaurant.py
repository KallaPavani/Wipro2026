import requests

BASE_URL = "http://localhost:5000/api/v1/restaurants"

# 1. Test Register Restaurant
def test_register_restaurant():
    response = requests.post(
        BASE_URL,
        json={
            "name": "Test Hotel",
            "category": "Indian",
            "location": "Hyderabad",
            "contact": "9999999999"
        }
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Hotel"


# 2. Test Duplicate Restaurant
def test_duplicate_restaurant():
    requests.post(BASE_URL, json={"name": "Test Hotel"})
    response = requests.post(BASE_URL, json={"name": "Test Hotel"})
    assert response.status_code == 409


# 3. Test Get Restaurant By ID
def test_list_restaurants():
    create = requests.post(BASE_URL, json={"name": "Test Hotel"})
    restaurant_id = create.json()["id"]

    response = requests.get(f"{BASE_URL}/{restaurant_id}")
    assert response.status_code == 200


# 4. Test Invalid Restaurant
def test_invalid_restaurant():
    response = requests.get(f"{BASE_URL}/999")
    assert response.status_code == 404


# 5. Test Update Restaurant
def test_update_restaurant():
    create = requests.post(BASE_URL, json={"name": "Test Hotel"})
    restaurant_id = create.json()["id"]

    response = requests.put(
        f"{BASE_URL}/{restaurant_id}",
        json={"name": "Taj Hotel(Updated)"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Taj Hotel(Updated)"


# 6. Test Disable Restaurant
def test_disable_restaurant():
    create = requests.post(BASE_URL, json={"name": "Test Hotel"})
    restaurant_id = create.json()["id"]

    response = requests.put(f"{BASE_URL}/{restaurant_id}/disable", json={})
    assert response.status_code == 200


# 7. Test Delete Restaurant
def test_delete_restaurant():
    create = requests.post(BASE_URL, json={"name": "Test Hotel"})
    restaurant_id = create.json()["id"]

    response = requests.delete(f"{BASE_URL}/{restaurant_id}")
    assert response.status_code == 200


# 8. Test Delete Invalid
def test_delete_invalid_restaurant():
    response = requests.delete(f"{BASE_URL}/999")
    assert response.status_code == 404

#9. Test Update invalid restaurant
def test_update_invalid_restaurant():
    response = requests.put(
        f"{BASE_URL}/99",
        json={"name": "No Hotel"}
    )
    assert response.status_code == 404
