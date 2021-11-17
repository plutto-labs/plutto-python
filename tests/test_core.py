import pytest

from plutto import Plutto
from plutto.client import Client
from plutto.mixins import ManagerMixin


class TestCorePluttoObject:
    def test_object_creations(self):
        api_key = "test_api_key"
        plutto = Plutto(api_key)
        assert isinstance(plutto._client, Client)

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

    def test_invoices_manager(self):
        # pylint: disable=protected-access
        api_key = "test_api_key"
        plutto = Plutto(api_key)

        assert plutto._Plutto__invoices_manager is None
        assert isinstance(plutto.invoices, ManagerMixin)
        assert plutto._Plutto__invoices_manager is not None
        assert isinstance(plutto._Plutto__invoices_manager, ManagerMixin)

        with pytest.raises(NameError):
            plutto.invoices = None

        assert plutto.invoices is not None
        assert isinstance(plutto.invoices, ManagerMixin)
        assert isinstance(plutto._Plutto__invoices_manager, ManagerMixin)

    def test_products_manager(self):
        # pylint: disable=protected-access
        api_key = "test_api_key"
        plutto = Plutto(api_key)

        assert plutto._Plutto__products_manager is None
        assert isinstance(plutto.products, ManagerMixin)
        assert plutto._Plutto__products_manager is not None
        assert isinstance(plutto._Plutto__products_manager, ManagerMixin)

        with pytest.raises(NameError):
            plutto.products = None

        assert plutto.products is not None
        assert isinstance(plutto.products, ManagerMixin)
        assert isinstance(plutto._Plutto__products_manager, ManagerMixin)

    def test_permission_groups(self):
        # pylint: disable=protected-access
        api_key = "test_api_key"
        plutto = Plutto(api_key)

        assert plutto._Plutto__permission_groups_manager is None
        assert isinstance(plutto.permission_groups, ManagerMixin)
        assert plutto._Plutto__permission_groups_manager is not None
        assert isinstance(plutto._Plutto__permission_groups_manager, ManagerMixin)

        with pytest.raises(NameError):
            plutto.permission_groups = None

        assert plutto.permission_groups is not None
        assert isinstance(plutto.permission_groups, ManagerMixin)
        assert isinstance(plutto._Plutto__permission_groups_manager, ManagerMixin)
