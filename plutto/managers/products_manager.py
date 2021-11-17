"""Module to hold the products manager."""

from plutto.mixins import ManagerMixin


class ProductsManager(ManagerMixin):
    """Class to hold the products manager."""

    resource = "product"
    methods = ["all"]
