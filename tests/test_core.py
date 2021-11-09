from plutto import Plutto
from plutto.client import Client
from plutto.mixins import ManagerMixin


class TestCorePluttoObject:
    def test_object_creations(self):
        api_key = "test_api_key"
        plutto = Plutto(api_key)
        assert isinstance(plutto._client, Client)
        assert isinstance(plutto.customers, ManagerMixin)
