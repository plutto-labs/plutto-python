"""Module to hold the invoices manager."""

from plutto.mixins import ManagerMixin
from plutto.resource_handlers import resource_patch
from plutto.utils import can_raise_http_error, get_resource_class


class InvoicesManager(ManagerMixin):
    """Class to hold the invoices manager."""

    resource = "invoice"
    methods = ["all", "get", "mark_as"]

    @can_raise_http_error
    def mark_as(self, unique_identifier, **kwargs):
        """Mark an invoice"""
        klass = get_resource_class(self.__class__.resource)
        object_ = resource_patch(
            client=self._client,
            path=self._path,
            id_=unique_identifier,
            action="mark_as",
            klass=klass,
            handlers=self._handlers,
            methods=self.__class__.methods,
            resource=self.__class__.resource,
            params=kwargs,
        )

        return object_
