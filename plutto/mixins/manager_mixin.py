"""Module to hold the mixin for the managers."""

from abc import ABCMeta, abstractmethod

class ManagerMixin(metaclass=ABCMeta):
    """Class to hold the mixin for the managers."""

    def __init__(self, path, client):
        self._path = path
        self._client = client
        self._handler = {
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

