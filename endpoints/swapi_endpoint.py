import requests

class swapi_endpoint:
    """ Page Object model for centralized endpoint for API testing """

    def __init__(self):
        self.base_url = "https://swapi.dev/api/" # Base URL for Swapi API

    # Gets all data of resource_type, with optional params: id, query
    def get_resource(self, resource_type: str, id=None, query=None):
        url = self.base_url + resource_type + '/'
        if id is not None:
            url += str(id) + '/'
        if query is not None:
            url += str(query) + '/'
        return requests.get(url)
    