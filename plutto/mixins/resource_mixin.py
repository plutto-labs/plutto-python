from abc import ABCMeta
from plutto.utils import get_resource_class, singularize, objetize

class ResourceMixin(metaclass=ABCMeta):

    """Represents the mixin for the resources."""

    mappings = {}
    resource_indetifier = "id"

    def __init__(self, client, handlers, methods, path, **kwargs):
        self._client = client
        self._handlers = handlers
        self._methods = methods
        self._path = path
        self._attributes = []
        for key, value in kwargs.items():
            try:
                resource = self.__class__.mappings.get(key, key)
                if isinstance(value, list):
                    resource = singularize(resource)
                    element = {} if not value else value[0]
                    klass = get_resource_class(resource, value=element)
                    setattr(self, key, [objetize(klass, client, x) for x in value])
                else:
                    klass = get_resource_class(resource, value=value)
                    setattr(self, key, objetize(klass, client, value))
                self._attributes.append(key)
            except NameError:
                pass

    def __getattr__(self, attr):
        if attr not in self._methods:
            raise AttributeError(
                f"{self.__class__.__name__} has no attribute {attr.lstrip('_')}"
            )
        return getattr(self, f"_{attr}")
