"""Module to hold the invoices manager."""

from plutto.mixins import ManagerMixin


class InvoicesManager(ManagerMixin):
    """Class to hold the invoices manager."""

    resource = "invoice"
    methods = ["all", "get"]
