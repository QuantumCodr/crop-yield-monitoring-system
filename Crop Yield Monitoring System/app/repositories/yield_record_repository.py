"""
------------------------------------------------------------
Program Name : Crop Yield Monitoring System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Yield Record Repository
Description  : Handles JSON storage and retrieval of
               YieldRecord objects.
------------------------------------------------------------
"""

import json

from app.models import YieldRecord


class YieldRecordRepository:
    """Handles persistence of YieldRecord objects."""

    def __init__(self, file_path):
        self.file_path = file_path

    def generate_id(self):
        """Generate the next available yield record ID."""
        data = self._load()

        if not data:
            return 1

        return max(int(key) for key in data.keys()) + 1

    def save(self, yield_record):
        """Save a YieldRecord object to the JSON file."""
        data = self._load()

        data[str(yield_record.yield_record_id)] = {
            "yield_record_id": yield_record.yield_record_id,
            "farmer_id": yield_record.farmer_id,
            "crop_id": yield_record.crop_id,
            "quantity": yield_record.quantity,
            "unit": yield_record.unit,
        }

        self._write(data)

    def find_by_id(self, yield_record_id):
        """Return a YieldRecord object by ID, or None if not found."""
        data = self._load()
        record_data = data.get(str(yield_record_id))

        if record_data is None:
            return None

        return YieldRecord(
            record_data["yield_record_id"],
            record_data["farmer_id"],
            record_data["crop_id"],
            record_data["quantity"],
            record_data["unit"],
        )

    def find_all(self):
        """Return all stored YieldRecord objects."""
        data = self._load()

        yield_records = {}

        for key, record_data in data.items():
            yield_records[key] = YieldRecord(
                record_data["yield_record_id"],
                record_data["farmer_id"],
                record_data["crop_id"],
                record_data["quantity"],
                record_data["unit"],
            )

        return yield_records

    def update(self, yield_record):
        """Update an existing YieldRecord in the JSON file."""
        data = self._load()
        record_key = str(yield_record.yield_record_id)

        if record_key not in data:
            return False

        data[record_key] = {
            "yield_record_id": yield_record.yield_record_id,
            "farmer_id": yield_record.farmer_id,
            "crop_id": yield_record.crop_id,
            "quantity": yield_record.quantity,
            "unit": yield_record.unit,
        }

        self._write(data)

        return True

    def _load(self):
        """Load yield record data from the JSON file."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _write(self, data):
        """Write yield record data to the JSON file."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)