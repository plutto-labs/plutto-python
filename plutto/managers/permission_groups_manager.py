"""Module to hold the permission groups manager."""

from plutto.mixins import ManagerMixin


class PermissionGroupsManager(ManagerMixin):
    """Class to hold the permission groups manager."""

    resource = "permission_group"
    methods = ["all"]
