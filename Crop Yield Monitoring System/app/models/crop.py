"""
------------------------------------------------------------
Program Name : Crop Yield Monitoring System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Crop Model
Description  : Defines the Crop class used to represent
               crops monitored by the system.
------------------------------------------------------------
"""


class Crop:
    """Represents a crop being monitored."""

    # Supported crop names used by the system.
    VALID_CROPS = {
        "Rice": "Rice",
        "Cassava": "Cassava",
        "Maize": "Maize",
        "Groundnut": "Groundnut",
        "Vegetable": "Vegetable",
        "Other": "Other",
    }

    # Supported crop lifecycles used by the system.
    VALID_LIFECYCLES = {
        "Short Cycle": "Short Cycle",
        "Medium Cycle": "Medium Cycle",
        "Long Cycle": "Long Cycle",
        "Year Round": "Year Round",
        "Other": "Other",
    }

    def __init__(self, crop_id, name, lifecycle):
        self.__crop_id = crop_id
        self.name = name
        self.lifecycle = lifecycle

    @property
    def crop_id(self):
        """Return the crop's unique identifier."""
        return self.__crop_id

    def display_info(self):
        """Return the crop's information as formatted text."""
        return (
            f"Crop ID: {self.crop_id}\n"
            f"Name: {self.name}\n"
            f"Lifecycle: {self.lifecycle}"
        )

    @classmethod
    def create_basic(cls, crop_id, name, lifecycle):
        """Create a basic Crop object."""
        return cls(crop_id, name, lifecycle)

    @staticmethod
    def is_valid_crop(crop_name):
        """Check whether a crop name is supported."""
        return crop_name in Crop.VALID_CROPS

    @staticmethod
    def is_valid_lifecycle(lifecycle):
        """Check whether a crop lifecycle is supported."""
        return lifecycle in Crop.VALID_LIFECYCLES