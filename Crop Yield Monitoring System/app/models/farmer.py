"""
------------------------------------------------------------
Program Name : Crop Yield Monitoring System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Farmer Model
Description  : Defines the Farmer class used to represent
               farmers participating in crop production.
------------------------------------------------------------
"""


class Farmer:
    """Represents a farmer in the crop yield monitoring system."""

    def __init__(self, farmer_id, name, location):
        self.__farmer_id = farmer_id
        self.name = name
        self.location = location

    @property
    def farmer_id(self):
        """Return the farmer's unique identifier."""
        return self.__farmer_id

    def display_info(self):
        """Return the farmer's information as formatted text."""
        return (
            f"Farmer ID: {self.farmer_id}\n"
            f"Name: {self.name}\n"
            f"Location: {self.location}"
        )