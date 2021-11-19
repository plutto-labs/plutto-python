"""Module to hold the customers manager."""

from plutto.mixins import ManagerMixin
from plutto.resource_handlers import resource_permission
from plutto.utils import can_raise_http_error, get_resource_class


class CustomersManager(ManagerMixin):
    """Class to hold the customers manager."""

    resource = "customer"
    methods = ["all", "get", "create", "update", "delete", "permission"]

    @can_raise_http_error
    def permission(self, unique_identifier, permission_name, **kwargs):
        """Check if the user has the permission with permission_name"""
        resource = "customer_permission"
        klass = get_resource_class(resource)
        object_ = resource_permission(
            client=self._client,
            path=self._path,
            id_=unique_identifier,
            permission_name=permission_name,
            klass=klass,
            resource=resource,
            params=kwargs,
        )

        return object_
