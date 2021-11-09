"""Module to hold the mixin for the managers."""

from abc import ABCMeta, abstractmethod

from plutto.resource_handlers import resource_all
from plutto.utils import get_resource_class, pluralize, can_raise_http_error

class ManagerMixin(metaclass=ABCMeta):
    """Class to hold the mixin for the managers."""

    def __init__(self, path, client):
        self._path = path
        self._client = client
        self._handlers = {
            "update": self.post_update_handler,
            "delete": self.post_delete_handler,
        }

    def __getattr__(self, attr):
        if attr not in self.__class__.methods:
            raise AttributeError(
                f"{self.__class__.__name__} has no attribute '{attr.lstrip('_')}'"
            )
        return getattr(self, f"_{attr}")

    @property
    @abstractmethod
    def resource(self):
        """
        This abstract property must be instanced as a class attribute
        when subclassing this mixin. It represents the name of the resource
        using snake_case.
        """

    @property
    @abstractmethod
    def methods(self):
        """
        This abstract property must be instanced as a class attribute
        when subclassing this mixin. It represents the methods that can be
        accessed using the manager. Must be an array with at leat one of:
        ['all', 'get', 'create', 'update', 'delete'].
        """

    @can_raise_http_error
    def _all(self, **kwargs):
        """
        Method to fetch all objects.

        :kwargs: can be used to filter the results using the API parameters.
        """
        klass = get_resource_class(self.__class__.resource)
        objects = resource_all(
            client=self._client,
            path=self._path,
            klass=klass,
            handlers=self._handlers,
            methods=self.__class__.methods,
            resource=pluralize(self.__class__.resource),
            params=kwargs,
        )
        return self.post_all_handler(objects, **kwargs)

    def post_all_handler(self, objects, **kwargs):
        """
        Hook that runs after the :all: method. Receives the objects fetched
        and **must** return them (either modified or as they came).
        """
        return objects

    def post_get_handler(self, object_, identifier, **kwargs):
        """
        Hook that runs after the :get: method. Receives the object fetched
        with its identifier and **must** return the object (either modified
        or as it came).
        """
        return object_

    def post_create_handler(self, object_, **kwargs):
        """
        Hook that runs after the :create: method. Receives the object fetched
        and **must** return the it (either modified or as it came).
        """
        return object_

    def post_update_handler(self, object_, identifier, **kwargs):
        """
        Hook that runs after the :update: method. Receives the object fetched
        with its identifier and **must** return the object (either modified
        or as it came).
        """
        return object_

    def post_delete_handler(self, identifier, **kwargs):
        """
        Hook that runs after the :create: method. Receives the identifier
        and **must** return it (either modified or as it came).
        """
        return identifier
