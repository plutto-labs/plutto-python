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
