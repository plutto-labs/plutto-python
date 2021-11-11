from types import GeneratorType

import httpx
import pytest

from plutto.client import Client


class TestClientCreationFunctionality:
    def setup_method(self):
        self.base_url = "https://test.com"
        self.api_key = "test_api_key"
        self.user_agent = "plutto-python/test"
        self.params = {"first_param": "value1", "second_param": "value2"}

    def create_client(self, params=False):
        if not params:
            return Client(self.base_url, self.api_key, self.user_agent)
        return Client(self.base_url, self.api_key, self.user_agent, params=self.params)

    def tests_client_creation_without_params(self):
        client = self.create_client()
        assert isinstance(client, Client)
        assert client.base_url == self.base_url
        assert client.api_key == self.api_key
        assert client.user_agent == self.user_agent
        assert client.params == {}

    def test_client_creation_with_params(self):
        client = self.create_client(params=True)
        assert isinstance(client, Client)
        assert client.base_url == self.base_url
        assert client.api_key == self.api_key
        assert client.user_agent == self.user_agent
        assert client.params == self.params

    def test_client_headers(self):
        client = self.create_client()
        assert isinstance(client, Client)
        assert len(client.headers.keys()) == 2
        assert "Authorization" in client.headers
        assert "User-Agent" in client.headers
        assert client.headers["Authorization"] == f"Bearer {self.api_key}"
        assert client.headers["User-Agent"] == self.user_agent

    def test_client_http_lazy_initialization(self):
        # httpx client must be created after the attribute is called
        client = self.create_client()
        assert client._Client__client is None
        assert isinstance(client._client, httpx.Client)
        assert isinstance(client._Client__client, httpx.Client)


class TestClientRequestFunctionality:
    @pytest.fixture(autouse=True)
    def patch_http_request(self, patch_http_client):
        pass

    def setup_method(self):
        self.base_url = "https://test.com"
        self.api_key = "super_secret_api_key"
        self.user_agent = "plutto-python/test"
        self.params = {"first_param": "value1", "second_param": "value2"}
        self.client = Client(
            self.base_url, self.api_key, self.user_agent, params=self.params
        )

    def test_paginated_request(self):
        data = self.client.request("/movements", paginated=True)
        assert isinstance(data, GeneratorType)

    def test_get_request(self):
        data = self.client.request("/movements/3", method="get")
        assert isinstance(data, dict)
        assert len(data.keys()) > 0
