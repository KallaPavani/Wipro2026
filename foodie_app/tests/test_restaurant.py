import requests

BASE_URL="http://localhost:5000/api/v1/restaurants"

#1. Test Register Restaurant(Positive)
def test_register_restaurant():
    response = requests.post(
        BASE_URL,
    json={
        "name": "Test Hotel",
        "category": "Indian",
        "location": "Hyderabad",
        "contact": "9999999999"
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Test Hotel"

#2. Test Duplicate Restaurant(Negative)
def test_duplicate_restaurant():
    response = requests.post(
        BASE_URL,
        json={
            "name": "Test Hotel"
        }
    )
    assert response.status_code == 409

#3. Test Get Restaurant By ID(Positive)
def test_list_restaurants():
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200
    assert "id" in response.json()

#4. Test Get Restaurant Invalid ID(Negative)
def test_invalid_restaurant():
    response = requests.get(f"{BASE_URL}/999")
    assert response.status_code == 404

#5.Test Update Restaurant(Positive)
def test_update_restaurant():
    response = requests.put(
        f"{BASE_URL}/1",
        json={"name": "Taj Hotel(Updated)"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Taj Hotel(Updated)"

#6. Test Update Invalid Restaurant(Negative)
def test_update_invalid_restaurant():
    response = requests.put(
        f"{BASE_URL}/99",
        json={"name": "No Hotel"}
    )
    assert response.status_code == 404

#5. Test Disable Restaurant
def test_disable_restaurant():
    response = requests.put(f"{BASE_URL}/1/disable", json={})
    assert response.status_code == 200
    assert response.json()["message"] == "Restaurant disabled"

#6. Test Delete Restaurant
def test_delete_restaurant():
    response = requests.delete(f"{BASE_URL}/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Restaurant deleted"

#7. Test Delete Invalid Restaurant(Negative)
def test_delete_invalid_restaurant():
    response = requests.delete(f"{BASE_URL}/999")
    assert response.status_code == 404