"""Module to hold the meter events manager."""

from plutto.mixins import ManagerMixin


class MeterEventsManager(ManagerMixin):
    """Class to hold the meter events manager."""

    resource = "meter_event"
    methods = ["create"]
