# Conceptual flow:
# 1. Load test data from CSV/JSOn
# 2. Send requests to the API endpoints using requests
# 3. Assert response status codes, headers and payload contents
# 4. Report results locally (via pytest console output)
# 5. Generate polished report for the dashboard and logs
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from endpoints.endpoint_factory import endpoint_factory
from resources.swapi_resources import swapi_resources

factory = endpoint_factory()
swapi_endpoint = factory.get_swapi_endpoint()

def test_get_people_luke_skywalker():
    '''
    Test fetching all the people in star wars API
    '''
    response = swapi_endpoint.get_resource(swapi_resources.PEOPLE, 1)
    assert response.status_code == 200

    data = response.json()
    assert data['name'] == 'Luke Skywalker'
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
    response = swapi_endpoint.get_resource(swapi_resources.PEOPLE)
    assert response.status_code == 200

    data = response.json()
    assert data['count'] == 82

