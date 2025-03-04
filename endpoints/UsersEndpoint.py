import requests

class UsersEndpoint:
    """ Page Object model for centralized endpoint for API testing """

    def __init__(self, base_url):
        self.base_url = base_url