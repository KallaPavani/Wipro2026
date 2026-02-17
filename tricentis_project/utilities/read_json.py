import json
import os

def read_test_data():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_path, "data", "test_data.json")

    with open(file_path, "r") as file:
        return json.load(file)
