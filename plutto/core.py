"""
Core module to house the Plutto object of the Plutto Python SDK.
"""

from plutto.client import Client
from plutto.constants import API_BASE_URL, API_VERSION
from plutto.managers import (
    CustomersManager,
    InvoicesManager,
    MeterEventsManager,
    SubscriptionsManager,
)
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
        self.__subscriptions_manager = None
        self.__meter_events_manager = None
        self.__invoices_manager = None

    @property
    def customers(self):
        """Proxies the customers manager."""
        if self.__customers_manager is None:
            self.__customers_manager = CustomersManager("/customers", self._client)

        return self.__customers_manager

    @customers.setter
    def customers(self, value):  # pylint: disable=no-self-use
        raise NameError("Attribute name corresponds to a manager")

    @property
    def subscriptions(self):
        """Proxies the subscriptions manager."""
        if self.__subscriptions_manager is None:
            self.__subscriptions_manager = SubscriptionsManager(
                "/subscriptions", self._client
            )

        return self.__subscriptions_manager

    @subscriptions.setter
    def subscriptions(self, value):  # pylint: disable=no-self-use
        raise NameError("Attribute name corresponds to a manager")

    @property
    def meter_events(self):
        """Proxies the meter events manager."""
        if self.__meter_events_manager is None:
            self.__meter_events_manager = MeterEventsManager(
                "/meter_events", self._client
            )

        return self.__meter_events_manager

    @meter_events.setter
    def meter_events(self, value):  # pylint: disable=no-self-use
        raise NameError("Attribute name corresponds to a manager")

    @property
    def invoices(self):
        """Proxies the invoices manager."""
        if self.__invoices_manager is None:
            self.__invoices_manager = InvoicesManager("/invoices", self._client)

        return self.__invoices_manager

    @invoices.setter
    def invoices(self, value):  # pylint: disable=no-self-use
        raise NameError("Attribute name corresponds to a manager")
