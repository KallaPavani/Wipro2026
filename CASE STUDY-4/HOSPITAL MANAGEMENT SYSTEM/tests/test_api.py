import requests

def test_add_patient(base_url):
    res = requests.post(f"{base_url}/api/patients", json={
        "name": "John",
        "age": 30,
        "gender": "Male",
        "contact": "9999999999",
        "disease": "Flu",
        "doctor": "Dr Smith"
    })
    assert res.status_code == 201

def test_get_patients(base_url):
    res = requests.get(f"{base_url}/api/patients")
    assert res.status_code == 200
    assert len(res.json()) > 0
