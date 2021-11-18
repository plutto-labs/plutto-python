import pytest

from plutto.client import Client
from plutto.managers import InvoicesManager
from plutto.mixins import ResourceMixin


class MockInvoicesManager(InvoicesManager):
    resource = "resource_doesnt_exist"


class TestInvoicesManager:
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
        self.manager = MockInvoicesManager(self.path, self.client)

    def test_mark_as(self):
        payload = {"status": "paid"}
        object_ = self.manager.mark_as("id", **payload)
        assert isinstance(object_, ResourceMixin)
