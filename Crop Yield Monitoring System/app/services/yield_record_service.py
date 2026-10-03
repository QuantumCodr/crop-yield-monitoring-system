"""
------------------------------------------------------------
Program Name : Crop Yield Monitoring System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Yield Record Service
Description  : Handles business operations for recording and
               updating crop yield information.
------------------------------------------------------------
"""

from app.models import YieldRecord


class YieldRecordService:
    """Provides application operations for yield records."""

    def __init__(
        self,
        yield_record_repository,
        farmer_repository,
        crop_repository
    ):
        self.yield_record_repository = yield_record_repository
        self.farmer_repository = farmer_repository
        self.crop_repository = crop_repository

    def record_yield(
        self,
        farmer_id,
        crop_id,
        quantity,
        unit
    ):
        """Create and save a new crop yield record."""

        farmer = self.farmer_repository.find_by_id(farmer_id)

        if farmer is None:
            raise ValueError("Farmer not found.")

        crop = self.crop_repository.find_by_id(crop_id)

        if crop is None:
            raise ValueError("Crop not found.")

        if quantity <= 0:
            raise ValueError("Yield quantity must be greater than zero.")

        if not unit.strip():
            raise ValueError("Yield unit cannot be empty.")

        yield_record_id = self.yield_record_repository.generate_id()

        yield_record = YieldRecord(
            yield_record_id,
            farmer_id,
            crop_id,
            quantity,
            unit.strip(),
        )

        self.yield_record_repository.save(yield_record)

        return yield_record

    def get_yield_record(self, yield_record_id):
        """Return a yield record by ID."""
        return self.yield_record_repository.find_by_id(
            yield_record_id
        )

    def get_all_yield_records(self):
        """Return all registered yield records."""
        return self.yield_record_repository.find_all()

    def get_yield_record_details(self, yield_record_id):
        """Return a yield record together with its crop details."""

        yield_record = self.yield_record_repository.find_by_id(
            yield_record_id
        )

        if yield_record is None:
            return None

        crop = self.crop_repository.find_by_id(
            yield_record.crop_id
        )

        return {
            "yield_record": yield_record,
            "crop": crop,
        }

    def get_all_yield_record_details(self):
        """Return all yield records together with crop details."""

        yield_records = (
            self.yield_record_repository.find_all()
        )

        yield_record_details = {}

        for key, yield_record in yield_records.items():
            crop = self.crop_repository.find_by_id(
                yield_record.crop_id
            )

            yield_record_details[key] = {
                "yield_record": yield_record,
                "crop": crop,
            }

        return yield_record_details

    def update_quantity(self, yield_record_id, quantity):
        """Update the quantity of an existing yield record."""

        if quantity <= 0:
            raise ValueError("Yield quantity must be greater than zero.")

        yield_record = self.yield_record_repository.find_by_id(
            yield_record_id
        )

        if yield_record is None:
            raise ValueError("Yield record not found.")

        yield_record.update_quantity(quantity)

        self.yield_record_repository.update(yield_record)

        return yield_record