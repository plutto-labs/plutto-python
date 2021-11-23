import datetime
from importlib import import_module

import httpx

from plutto.errors import PluttoError


def singularize(string):
    """Remove the last 's' from a string if exists."""
    return string.rstrip("s")


def pluralize(string):
    """Add an 's' to a string if it doesn't already end with 's'."""
    if string.endswith("s"):
        return string
    return string + "s"


def snake_to_pascal(snake_string):
    """Convert a snake_case string to PascalCase."""
    return "".join(word.title() for word in snake_string.split("_"))


def get_resource_class(snake_resource_name, value={}):
    """
    Get the class that corresponds to a resource using its
    name (in snake case) and it's value.
    """
    if isinstance(value, dict):
        module = import_module("plutto.resources")
        try:
            return getattr(module, snake_to_pascal(snake_resource_name))
        except AttributeError:
            return getattr(module, "GenericPluttoResource")
    return type(value)


def get_error_class(function):
    """
    Given an error name (in snake case), return the appropiate
    error class.
    """
    module = import_module("plutto.errors")
    return getattr(module, snake_to_pascal(function), PluttoError)


def can_raise_http_error(function):
    """
    Decorator that catches HTTPError exceptions and raises custom
    Plutto errors instead.
    """

    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except httpx.HTTPError as e:
            error_data = e.response.json()
            error = get_error_class(error_data["error"]["type"])
            raise error(error_data["error"]) from None

    return wrapper


def serialize(object_):
    """Serialize an object."""
    if callable(getattr(object_, "serialize", None)):
        return object_.serialize()
    if isinstance(object_, datetime.datetime):
        return object_.isoformat()
    return object_


def objetize(klass, client, data, handlers={}, methods=[], path=None):
    """Transform the :data: object into an object with class :klass:"""
    if data is None:
        return None
    if klass in [str, int, dict, float, bool]:
        return klass(data)
    return klass(client, handlers, methods, path, **data)


def objetize_generator(generator, klass, client, handlers={}, methods=[], path=None):
    """
    Transform a generator of dictionaries into a generator of
    objects with class :klass:.
    """
    for element in generator:
        yield objetize(klass, client, element, handlers, methods, path)
