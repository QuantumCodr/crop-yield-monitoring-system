"""
------------------------------------------------------------
Program Name : Crop Yield Monitoring System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Yield Record Model
Description  : Defines the YieldRecord class used to record
               the quantity of crop produced by a farmer.
------------------------------------------------------------
"""


class YieldRecord:
    """Represents a crop yield record."""

    def __init__(
        self,
        yield_record_id,
        farmer_id,
        crop_id,
        quantity,
        unit
    ):
        self.__yield_record_id = yield_record_id
        self.farmer_id = farmer_id
        self.crop_id = crop_id
        self.quantity = quantity
        self.unit = unit

    @property
    def yield_record_id(self):
        """Return the yield record's unique identifier."""
        return self.__yield_record_id

    def update_quantity(self, quantity):
        """Update the recorded quantity of crop produced."""
        self.quantity = quantity

    def display_info(self):
        """Return the yield record as formatted text."""
        return (
            f"Yield Record ID: {self.yield_record_id}\n"
            f"Farmer ID: {self.farmer_id}\n"
            f"Crop ID: {self.crop_id}\n"
            f"Quantity: {self.quantity}\n"
            f"Unit: {self.unit}"
        )