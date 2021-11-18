import pytest

from plutto.client import Client
from plutto.managers import SubscriptionsManager
from plutto.mixins import ResourceMixin


class MockSubscriptionsManager(SubscriptionsManager):
    resource = "resource_doesnt_exist"


class TestSubscriptionsManagerMethods:
    @pytest.fixture(autouse=True)
    def patch_http_client(self, patch_http_client):
        pass

    def setup_method(self):
        self.base_url = "https://test.com"
        self.api_key = "super_secret_api_key"
        self.user_agent = "plutto-python/test"
        self.params = {"first_param": "value1", "second_param": "value2"}
        self.client = Client(
            base_url=self.base_url,
            api_key=self.api_key,
            user_agent=self.user_agent,
            params=self.params,
        )
        self.path = "/resources"
        self.manager = MockSubscriptionsManager(self.path, self.client)

    def test_end_test(self):
        object_ = self.manager.end("id")
        assert isinstance(object_, ResourceMixin)

    def test_add_one_pricing(self):
        payload = {"princing_ids": ["pricing_id"]}
        object_ = self.manager.add_pricings("id", **payload)
        assert isinstance(object_, ResourceMixin)

    def test_add_many_pricings(self):
        payload = {"pricing_ids": ["pricing_id_1", "pricing_id_2", "pricing_id_3"]}
        object_ = self.manager.add_pricings("id", **payload)
        assert isinstance(object_, ResourceMixin)

    def test_remove_one_pricing(self):
        payload = {"princing_ids": ["pricing_id"]}
        object_ = self.manager.remove_pricings("id", **payload)
        assert isinstance(object_, ResourceMixin)

    def test_remove_many_pricings(self):
        payload = {"pricing_ids": ["pricing_id_1", "pricing_id_2", "pricing_id_3"]}
        object_ = self.manager.remove_pricings("id", **payload)
        assert isinstance(object_, ResourceMixin)
