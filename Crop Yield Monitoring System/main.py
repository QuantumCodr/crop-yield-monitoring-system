"""
------------------------------------------------------------
Program Name : Crop Yield Monitoring System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : Application Entry Point
Description  : Creates the application dependencies and
               starts the Crop Yield Monitoring System.
------------------------------------------------------------
"""

from pathlib import Path

from app.cli import Application
from app.repositories import (
    FarmerRepository,
    CropRepository,
    YieldRecordRepository,
)
from app.services import (
    FarmerService,
    CropService,
    YieldRecordService,
)


# Build the data directory relative to this main.py file.
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

FARMER_FILE = DATA_DIR / "farmers.json"
CROP_FILE = DATA_DIR / "crops.json"
YIELD_RECORD_FILE = DATA_DIR / "yield_records.json"


def main():
    """Create application dependencies and start the system."""

    farmer_repository = FarmerRepository(FARMER_FILE)
    crop_repository = CropRepository(CROP_FILE)
    yield_record_repository = YieldRecordRepository(
        YIELD_RECORD_FILE
    )

    farmer_service = FarmerService(farmer_repository)
    crop_service = CropService(crop_repository)

    yield_record_service = YieldRecordService(
        yield_record_repository,
        farmer_repository,
        crop_repository,
    )

    application = Application(
        farmer_service,
        crop_service,
        yield_record_service,
    )

    application.run()


if __name__ == "__main__":
    main()