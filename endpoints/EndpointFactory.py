from endpoints.UsersEndpoint import UsersEndpoint

class EndpointFactory:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_users_endpoint(self):
        return UsersEndpoint(self.base_url)
    
    