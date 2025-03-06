# Conceptual flow:
# 1. Load test data from CSV/JSOn
# 2. Send requests to the API endpoints using requests
# 3. Assert response status codes, headers and payload contents
# 4. Report results locally (via pytest console output)
# 5. Generate polished report for the dashboard and logs

import pytest
import json
import sys
from pathlib import Path
from endpoints.endpoint_factory import endpoint_factory

factory = endpoint_factory()
swapi_endpoint = factory.get_swapi_endpoint()
DATA_FILE = Path("data/swapi_test_people.json")

def load_test_data():
    '''
    Reads JSON file and returns list of test cases
    '''
    with DATA_FILE.open("r", encoding='utf-8') as f:
        data = json.load(f)
    return data["tests"]

@pytest.mark.parametrize("test_case", load_test_data())
def test_get_people(test_case):
    '''
    Test fetching all the people in star wars API
    '''
    # Get the resources needed
    resource_str = test_case["resource"]
    item_id = test_case["item_id"]
    expected_name = test_case["expected_name"]

    response = swapi_endpoint.get_resource(resource_str, item_id)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    assert data['name'] == expected_name
    expected_keys = {
        "name", "height", "mass", "hair_color", 
        "skin_color", "eye_color", "birth_year", 
        "gender", "homeworld", "films", "species", 
        "vehicles", "starships", "created", 
        "edited", "url"
    }
    assert expected_keys.issubset(data.keys()),  \
           f"Some expected keys are missing: {expected_keys - data.keys()}"

def test_get_all_people():
    response = swapi_endpoint.get_resource("people")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    assert data['count'] == 82

def test_invalid_person_id():
    response = swapi_endpoint.get_resource("people", sys.maxsize)
    assert response.status_code == 404





