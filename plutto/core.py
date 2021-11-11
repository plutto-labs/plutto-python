"""
Core module to house the Plutto object of the Plutto Python SDK.
"""

from plutto.client import Client
from plutto.constants import API_BASE_URL, API_VERSION
from plutto.managers import CustomersManager
from plutto.version import __version__


class Plutto:

    """Encapsulates the core object's behaviour and methods."""

    def __init__(self, api_key):
        self._client = Client(
            base_url=f"{API_BASE_URL}/{API_VERSION}",
            api_key=api_key,
            user_agent=f"plutto-python/{__version__}",
        )

        self.__customers_manager = None

    @property
    def customers(self):
        """Proxies the customers manager."""
        if self.__customers_manager is None:
            self.__customers_manager = CustomersManager("/customers", self._client)

        return self.__customers_manager

    @customers.setter
    def customers(self, value):  # pylint: disable=no-self-use
        raise NameError("Attribute name corresponds to a manager")
