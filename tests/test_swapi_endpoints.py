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
DATA_FILE = Path("data/swapi_tests.json")

def load_test_data(resource):
    '''
    Reads JSON file and returns list of test cases
    '''
    with DATA_FILE.open("r", encoding='utf-8') as f:
        data = json.load(f)
    return data[resource]

'''
TEST PEOPLE
'''
@pytest.mark.parametrize("test_case", load_test_data("people"))
def test_get_people(test_case):
    '''
    Test fetching all the people in star wars API
    '''
    # Get the resources needed
    resource_str = "people"
    item_id = test_case["item_id"]
    values = test_case["values"]

    response = swapi_endpoint.get_resource(resource_str, item_id)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    expected_keys = {
        "name", "height", "mass", "hair_color", 
        "skin_color", "eye_color", "birth_year", 
        "gender", "homeworld", "films", "species", 
        "vehicles", "starships", "created", 
        "edited", "url"
    }
    assert expected_keys.issubset(data.keys()),  \
           f"Some expected keys are missing: {expected_keys - data.keys()}"
    for key in values.keys():
        assert values[key] == data[key]


def test_get_all_people():
    response = swapi_endpoint.get_resource("people")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    assert data['count'] == 82

def test_invalid_person_id():
    response = swapi_endpoint.get_resource("people", 84)
    assert response.status_code == 404

    response = swapi_endpoint.get_resource("people", 0)
    assert response.status_code == 404

    response = swapi_endpoint.get_resource("people", -1)
    assert response.status_code == 404

'''
TEST PLANETS
'''

@pytest.mark.parametrize("test_case", load_test_data("planets"))
def test_get_planets(test_case):
    '''
    Test fetching all the people in star wars API
    '''
    # Get the resources needed
    resource_str = "planets"
    item_id = test_case["item_id"]
    values = test_case["values"]

    response = swapi_endpoint.get_resource(resource_str, item_id)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    expected_keys = {
        "name", "diameter", "rotation_period", "orbital_period", "gravity", "population",
        "climate", "terrain", "surface_water", "residents", "films", "url", "created", "edited"
    }
    assert expected_keys.issubset(data.keys()),  \
           f"Some expected keys are missing: {expected_keys - data.keys()}"
    for key in values.keys():
        assert values[key].lower() == data[key].lower()


def test_get_all_planets():
    response = swapi_endpoint.get_resource("planets")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    assert data['count'] == 60

def test_invalid_planet_id():
    response = swapi_endpoint.get_resource("planets", 0)
    assert response.status_code == 404

    response = swapi_endpoint.get_resource("planets", 62)
    assert response.status_code == 404

    response = swapi_endpoint.get_resource("planets", sys.maxsize)
    assert response.status_code == 404

    response = swapi_endpoint.get_resource("planets", -1)
    assert response.status_code == 404

'''
FILMS
'''
@pytest.mark.parametrize("test_case", load_test_data("films"))
def test_get_people(test_case):
    '''
    Test fetching all the films in star wars API
    '''
    # Get the resources needed
    resource_str = "films"
    item_id = test_case["item_id"]
    values = test_case["values"]

    response = swapi_endpoint.get_resource(resource_str, item_id)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    expected_keys = {
        "title", "episode_id", "opening_crawl", "director", "producer", "release_date",
        "species", "starships", "vehicles", "characters", "planets", "url", "created", "edited"
    }
    assert expected_keys.issubset(data.keys()),  \
           f"Some expected keys are missing: {expected_keys - data.keys()}"
    for key in values.keys():
        assert values[key] == data[key]


def test_get_all_films():
    response = swapi_endpoint.get_resource("films")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    assert data['count'] == 6

def test_invalid_films_id():
    response = swapi_endpoint.get_resource("films", 7)
    assert response.status_code == 404

    response = swapi_endpoint.get_resource("films", 0)
    assert response.status_code == 404

    response = swapi_endpoint.get_resource("films", -1)
    assert response.status_code == 404