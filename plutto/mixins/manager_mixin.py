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

