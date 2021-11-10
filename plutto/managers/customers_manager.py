"""Module to hold the customers manager."""

from plutto.mixins.manager_mixin import ManagerMixin


class CustomersManager(ManagerMixin):
    """Class to hold the customers manager."""

    resource = "customer"
    methods = ["all", "get", "create", "update", "delete"]
