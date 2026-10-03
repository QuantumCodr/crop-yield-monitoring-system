"""
------------------------------------------------------------
Program Name : Crop Yield Monitoring System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Crop Repository
Description  : Handles JSON storage and retrieval of Crop
               objects.
------------------------------------------------------------
"""

import json

from app.models import Crop


class CropRepository:
    """Handles persistence of Crop objects."""

    def __init__(self, file_path):
        self.file_path = file_path

    def generate_id(self):
        """Generate the next available crop ID."""
        data = self._load()

        if not data:
            return 1

        return max(int(key) for key in data.keys()) + 1

    def save(self, crop):
        """Save a Crop object to the JSON file."""
        data = self._load()

        data[str(crop.crop_id)] = {
            "crop_id": crop.crop_id,
            "name": crop.name,
            "lifecycle": crop.lifecycle,
        }

        self._write(data)

    def find_by_id(self, crop_id):
        """Return a Crop object by ID, or None if not found."""
        data = self._load()
        crop_data = data.get(str(crop_id))

        if crop_data is None:
            return None

        return Crop(
            crop_data["crop_id"],
            crop_data["name"],
            crop_data["lifecycle"],
        )

    def find_all(self):
        """Return all stored Crop objects."""
        data = self._load()

        crops = {}

        for key, crop_data in data.items():
            crops[key] = Crop(
                crop_data["crop_id"],
                crop_data["name"],
                crop_data["lifecycle"],
            )

        return crops

    def _load(self):
        """Load crop data from the JSON file."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _write(self, data):
        """Write crop data to the JSON file."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)