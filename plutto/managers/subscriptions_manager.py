"""Module to hold the subscriptions manager."""

from plutto.mixins import ManagerMixin
from plutto.resource_handlers import resource_patch
from plutto.utils import can_raise_http_error, get_resource_class


class SubscriptionsManager(ManagerMixin):
    """Class to hold the subscriptions manager."""

    resource = "subscription"
    methods = ["get", "create", "end"]

    @can_raise_http_error
    def end(self, unique_identifier, **kwargs):
        klass = get_resource_class(self.__class__.resource)
        object_ = resource_patch(
            client=self._client,
            path=self._path,
            id_=unique_identifier,
            action="end_subscription",
            klass=klass,
            handlers=self._handlers,
            methods=self.__class__.methods,
            resource=self.__class__.resource,
            params=kwargs,
        )

        return object_
