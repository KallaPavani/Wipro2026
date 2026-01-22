import requests
import json

# 1️. API URL (Public REST API)
url = "https://jsonplaceholder.typicode.com/users"

# 2️. Custom headers
headers = {
    "User-Agent": "Python-Requests-Demo",
    "Accept": "application/json"
}

try:
    #GET request
    response = requests.get(url, headers=headers, timeout=10)

    #Handling HTTP errors
    response.raise_for_status()

    #Parsing JSON response
    users = response.json()

    extracted_data = []
    for user in users:
        extracted_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"]
        })

    #Saving extracted data into a JSON file
    with open("users_data.json", "w", encoding="utf-8") as file:
        json.dump(extracted_data, file, indent=4)

    print("Data successfully fetched and saved to users_data.json")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the server")

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.RequestException as err:
    print(f"Request error: {err}")

except Exception as e:
    print(f"Unexpected error: {e}")
