import pytest
from decouple import config

from plutto.client import Client
from plutto.mixins import ManagerMixin, ResourceMixin


class InvalidMethodsMockManager(ManagerMixin):
    resource = "resource_doesnt_exist"


class InvalidResourceMockManager(ManagerMixin):
    methods = ["all", "get", "create", "update", "delete"]


class IncompleteMockManager(ManagerMixin):
    resource = "resource_doesnt_exist"
    methods = ["get", "update"]


class EmptyMockManager(ManagerMixin):
    resource = "resource_doesnt_exist"
    methods = ["all", "get", "create", "update", "delete"]


class ComplexMockManager(ManagerMixin):
    resource = "resource_doesnt_exist"
    methods = ["all", "get", "create", "update", "delete"]

    def post_all_handler(self, objects, **kwargs):
        print("Executing the 'post all' handler")
        return objects

    def post_get_handler(self, object_, **kwargs):
        print("Executing the 'post get' handler")
        return object_

    def post_create_handler(self, object_, **kwargs):
        print("Executing the 'post create' handler")
        return object_

    def post_update_handler(self, object_, identifier, **kwargs):
        print("Executing the 'post update' handler")
        return object_

    def post_delete_handler(self, identifier, **kwargs):
        print("Executing the 'post delete' handler")
        return identifier


class TestManagerMixinCreation:
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

    def test_invalid_methods(self):
        with pytest.raises(TypeError):
            InvalidMethodsMockManager(self.path, self.client)

    def test_invalid_resource(self):
        with pytest.raises(TypeError):
            InvalidResourceMockManager(self.path, self.client)

    def test_calling_invalid_methods(self):
        manager = IncompleteMockManager(self.path, self.client)
        with pytest.raises(AttributeError):
            manager.all()

    def test_calling_valid_methods(self):
        manager = IncompleteMockManager(self.path, self.client)
        manager.get("id")


class TestManagerMixinMethods:
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
        self.manager = EmptyMockManager(self.path, self.client)

    def test_all_not_lazy_method(self):
        objects = self.manager.all(lazy=False)
        assert isinstance(objects, list)
        for object_ in objects:
            assert isinstance(object_, ResourceMixin)


class TestManagerMixinHandlers:
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
        self.manager = ComplexMockManager(self.path, self.client)

    def test_all_handler(self, capsys):
        self.manager.all()
        captured = capsys.readouterr().out
        assert "all" in captured
