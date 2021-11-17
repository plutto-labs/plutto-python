import pytest

from plutto import Plutto
from plutto.client import Client
from plutto.mixins import ManagerMixin


class TestCorePluttoObject:
    def test_object_creations(self):
        api_key = "test_api_key"
        plutto = Plutto(api_key)
        assert isinstance(plutto._client, Client)
        assert isinstance(plutto.customers, ManagerMixin)

    def test_customers_manager(self):
        # pylint: disable=protected-access
        api_key = "test_api_key"
        plutto = Plutto(api_key)

        assert plutto._Plutto__customers_manager is None
        assert isinstance(plutto.customers, ManagerMixin)
        assert plutto._Plutto__customers_manager is not None
        assert isinstance(plutto._Plutto__customers_manager, ManagerMixin)

        with pytest.raises(NameError):
            plutto.customers = None

        assert plutto.customers is not None
        assert isinstance(plutto.customers, ManagerMixin)
        assert isinstance(plutto._Plutto__customers_manager, ManagerMixin)

    def test_subscriptions_manager(self):
        # pylint: disable=protected-access
        api_key = "test_api_key"
        plutto = Plutto(api_key)

        assert plutto._Plutto__subscriptions_manager is None
        assert isinstance(plutto.subscriptions, ManagerMixin)
        assert plutto._Plutto__subscriptions_manager is not None
        assert isinstance(plutto._Plutto__subscriptions_manager, ManagerMixin)

        with pytest.raises(NameError):
            plutto.subscriptions = None

        assert plutto.subscriptions is not None
        assert isinstance(plutto.subscriptions, ManagerMixin)
        assert isinstance(plutto._Plutto__subscriptions_manager, ManagerMixin)

    def test_meter_events_manager(self):
        # pylint: disable=protected-access
        api_key = "test_api_key"
        plutto = Plutto(api_key)

        assert plutto._Plutto__meter_events_manager is None
        assert isinstance(plutto.meter_events, ManagerMixin)
        assert plutto._Plutto__meter_events_manager is not None
        assert isinstance(plutto._Plutto__meter_events_manager, ManagerMixin)

        with pytest.raises(NameError):
            plutto.meter_events = None

        assert plutto.meter_events is not None
        assert isinstance(plutto.meter_events, ManagerMixin)
        assert isinstance(plutto._Plutto__meter_events_manager, ManagerMixin)
