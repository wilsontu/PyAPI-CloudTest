from endpoints.swapi_endpoint import swapi_endpoint

class endpoint_factory:
    def __init__(self):
        pass

    def get_swapi_endpoint(self) -> swapi_endpoint:
        return swapi_endpoint()
    
    