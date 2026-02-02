import requests

def test_add_movie(base_url):
    payload={
        "id": 101,
        "movie_name": "Suits",
        "language": "English",
        "duration": "2h 49m"
    }
    response = requests.post(f"{base_url}/api/movies", json=payload)
    assert response.status_code == 201

def test_get_movies(base_url):
    response = requests.get(f"{base_url}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)