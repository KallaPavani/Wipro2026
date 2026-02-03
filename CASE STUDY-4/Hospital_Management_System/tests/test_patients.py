import requests

def test_add_patient(base_url):
    data = {
        "name": "John Doe",
        "age": 30,
        "gender": "Male",
        "contact": "1234567890",
        "disease": "Flu",
        "doctor": "Dr. Smith"
    }
    response = requests.post(f"{base_url}/api/patients", json=data)
    assert response.status_code == 201
    res_json = response.json()
    assert res_json["name"] == "John Doe"

def test_get_all_patients(base_url):
    response = requests.get(f"{base_url}/api/patients")
    assert response.status_code == 200
    res_json = response.json()
    assert isinstance(res_json, list)

def test_get_single_patient(base_url):
    response = requests.get(f"{base_url}/api/patients/1")
    assert response.status_code == 200
    res_json = response.json()
    assert res_json["id"] == 1

def test_update_patient(base_url):
    data = {"disease": "Cold"}
    response = requests.put(f"{base_url}/api/patients/1", json=data)
    assert response.status_code == 200
    res_json = response.json()
    assert res_json["disease"] == "Cold"

def test_delete_patient(base_url):
    response = requests.delete(f"{base_url}/api/patients/1")
    assert response.status_code == 200
    res_json = response.json()
    assert res_json["message"] == "Patient deleted successfully"