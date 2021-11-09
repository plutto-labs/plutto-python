import httpx
import pytest

from plutto.errors import PluttoError, AuthenticationError
from plutto.resources import Customer
from plutto.utils import (
    can_raise_http_error,
    singularize,
    pluralize,
    snake_to_pascal,
    get_resource_class,
    get_error_class,
    objetize,
)


class TestSnakeToPascal:
    def test_simple_string(self):
        snake = "this_is_a_test"
        pascal = snake_to_pascal(snake)
        assert pascal == "ThisIsATest"

    def test_complex_string(self):
        snake = "THIs_IS_a_TeSt"
        pascal = snake_to_pascal(snake)
        assert pascal == "ThisIsATest"


class TestSingularize:
    def test_plural_string(self):
        string = "customers"
        singular = singularize(string)
        assert singular == "customer"

    def test_singular_string(self):
        string = "customer"
        singular = singularize(string)
        assert singular == "customer"

    def test_complex_plural_dont_work(self):
        string = "knives"
        singular = singularize(string)
        assert singular != "knife"


class TestPluralize:
    def test_singular_string(self):
        string = "customer"
        plural = pluralize(string)
        assert plural == "customers"

    def test_plural_string(self):
        string = "customers"
        plural = pluralize(string)
        assert plural == "customers"

    def test_complex_singular_dont_work(self):
        string = "knife"
        plural = pluralize(string)
        assert plural != "knives"


class TestGetResourceClass:
    def test_default_valid_resource(self):
        resource = "customer"
        resource_class = get_resource_class(resource)
        assert resource_class == Customer

    def test_string_resource(self):
        resource = "anyone"
        klass = get_resource_class(resource, value="value")
        assert klass is str

    def test_int_resource(self):
        resource = "anyone"
        klass = get_resource_class(resource, value=1)
        assert klass is int

    def test_bool_resource(self):
        resource = "anyone"
        klass = get_resource_class(resource, value=True)
        assert klass is bool


class TestGetErrorClass:
    def test_valid_error(self):
        error_name = "authentication_error"
        error = get_error_class(error_name)
        assert error is AuthenticationError

    def test_invalid_error(self):
        error_name = "invalid_error"
        error = get_error_class(error_name)
        assert error is PluttoError


class TestCanRaiseHTTPError:
    @pytest.fixture(autouse=True)
    def setup(self):
        def no_error():
            pass

        def raise_http_error():
            raise httpx.HTTPError("F")

        def raise_generic_error():
            raise ValueError("Not HTTP Error")

        self.no_error = no_error
        self.raise_http_error = raise_http_error
        self.raise_generic_error = raise_generic_error

    def test_no_error(self):
        wrapped = can_raise_http_error(self.no_error)
        wrapped()

    def test_http_error(self):
        wrapped = can_raise_http_error(self.raise_http_error)
        with pytest.raises(Exception) as excinfo:
            wrapped()
        assert not isinstance(excinfo.value, PluttoError)


class ExampleClass:
    def __init__(self, client, handlers, methods, path, **kwargs):
        self.client = client
        self.handlers = handlers
        self.methods = methods
        self.path = path
        self.data = kwargs

class TestObjetize:
    def setup_method(self):
        self.client = "This is a client"
        self.data = {
            "id": "customer_rk18904983",
            "name": "Lord Valdomero",
            "address": "742 Evergreen Terrace",
        }

    def test_string_objetization(self):
        data = "This is string"
        object_ = objetize(str, self.client, data)
        assert isinstance(object_, str)
        assert object_ == data

    def test_dictionary_objetization(self):
        object_ = objetize(dict, self.client, self.data)
        assert isinstance(object_, dict)
        assert object_ == self.data

    def test_complete_objetization(self):
        object_ = objetize(ExampleClass, self.client, self.data)
        assert isinstance(object_, ExampleClass)
        assert object_.data["name"] == self.data["name"]
