"""
Module to house the Client object of the Plutto Python SDK.
"""

class Client:
    """Encapsulates the client behaviour and methods."""

    def __init__(self, base_url, api_key, user_agent, params={}):
        """Initializes the client object."""
        self.base_url = base_url
        self.api_key = api_key
        self.user_agent = user_agent
        self.params = params
        self.__client = None
