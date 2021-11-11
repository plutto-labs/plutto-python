"""
Module to house the Client object of the Plutto Python SDK.
"""

from json.decoder import JSONDecodeError

import httpx

from plutto.paginator import paginate


class Client:
    """Encapsulates the client behaviour and methods."""

    def __init__(self, base_url, api_key, user_agent, params={}):
        """Initializes the client object."""
        self.base_url = base_url
        self.api_key = api_key
        self.user_agent = user_agent
        self.params = params
        self.__client = None

    @property
    def _client(self):
        """Gets the client object."""
        if self.__client is None:
            self.__client = httpx.Client(
                base_url=self.base_url,
                headers=self.headers,
                params=self.params,
            )
        return self.__client

    @property
    def headers(self):
        """Gets the headers for the client."""
        return {
            "User-Agent": self.user_agent,
            "Authorization": f"Bearer {self.api_key}",
        }

    def request(
        self, path, paginated=False, method="get", params=None, json=None, resource=None
    ):
        """
        Uses the internal httpx client to make a simple request.
        """
        if paginated:
            return paginate(self._client, path, resource, params=params)

        response = self._client.request(method, path, params=params, json=json)
        response.raise_for_status()

        try:
            return response.json()
        except JSONDecodeError:
            return {}
