"""
------------------------------------------------------------
Program Name : Crop Yield Monitoring System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Crop Service
Description  : Handles business operations related to
               crop registration and retrieval.
------------------------------------------------------------
"""

from app.models import Crop


class CropService:
    """Provides application operations for crops."""

    def __init__(self, crop_repository):
        self.crop_repository = crop_repository

    def register_crop(self, name, lifecycle):
        """Create and save a new crop."""
        if not name.strip():
            raise ValueError("Crop name cannot be empty.")

        if not lifecycle.strip():
            raise ValueError("Crop lifecycle cannot be empty.")

        if not Crop.is_valid_crop(name.strip()):
            raise ValueError("Invalid crop type.")

        if not Crop.is_valid_lifecycle(lifecycle.strip()):
            raise ValueError("Invalid crop lifecycle.")

        crop_id = self.crop_repository.generate_id()

        crop = Crop.create_basic(
            crop_id,
            name.strip(),
            lifecycle.strip(),
        )

        self.crop_repository.save(crop)

        return crop

    def get_crop(self, crop_id):
        """Return a crop by ID."""
        return self.crop_repository.find_by_id(crop_id)

    def get_all_crops(self):
        """Return all registered crops."""
        return self.crop_repository.find_all()