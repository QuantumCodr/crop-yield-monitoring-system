"""
------------------------------------------------------------
Program Name : Crop Yield Monitoring System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : CLI Handlers
Description  : Handles user input and presentation for the
               Crop Yield Monitoring System.
------------------------------------------------------------
"""


class CLIHandlers:
    """Handles user interaction with application services."""

    def __init__(
        self,
        farmer_service,
        crop_service,
        yield_record_service
    ):
        self.farmer_service = farmer_service
        self.crop_service = crop_service
        self.yield_record_service = yield_record_service

    def register_farmer(self):
        """Register a new farmer."""
        print("\n--- Register Farmer ---")

        name = input("Enter farmer name: ").strip()
        location = input("Enter farmer location: ").strip()

        try:
            farmer = self.farmer_service.register_farmer(
                name,
                location,
            )

            print("\nFarmer registered successfully.")
            print(farmer.display_info())

        except ValueError as error:
            print(f"\nError: {error}")

    def register_crop(self):
        """Register a new crop."""
        print("\n--- Register Crop ---")

        print("\nSelect crop type:")
        print("1. Rice")
        print("2. Cassava")
        print("3. Maize")
        print("4. Groundnut")
        print("5. Vegetable")
        print("6. Other")

        crop_choices = {
            "1": "Rice",
            "2": "Cassava",
            "3": "Maize",
            "4": "Groundnut",
            "5": "Vegetable",
            "6": "Other",
        }

        crop_choice = input("Enter crop choice: ").strip()
        crop_name = crop_choices.get(crop_choice)

        if crop_name is None:
            print("\nInvalid crop choice.")
            return

        print("\nSelect crop lifecycle:")
        print("1. Short Cycle")
        print("2. Medium Cycle")
        print("3. Long Cycle")
        print("4. Year Round")
        print("5. Other")

        lifecycle_choices = {
            "1": "Short Cycle",
            "2": "Medium Cycle",
            "3": "Long Cycle",
            "4": "Year Round",
            "5": "Other",
        }

        lifecycle_choice = input(
            "Enter lifecycle choice: "
        ).strip()

        lifecycle = lifecycle_choices.get(lifecycle_choice)

        if lifecycle is None:
            print("\nInvalid lifecycle choice.")
            return

        try:
            crop = self.crop_service.register_crop(
                crop_name,
                lifecycle,
            )

            print("\nCrop registered successfully.")
            print(crop.display_info())

        except ValueError as error:
            print(f"\nError: {error}")

    def record_crop_yield(self):
        """Record a new crop yield."""
        print("\n--- Record Crop Yield ---")

        farmer_id = self._read_id("Enter farmer ID: ")
        crop_id = self._read_id("Enter crop ID: ")

        try:
            quantity = float(
                input("Enter yield quantity: ").strip()
            )
        except ValueError:
            print("\nInvalid quantity.")
            return

        unit = input("Enter yield unit: ").strip()

        try:
            yield_record = self.yield_record_service.record_yield(
                farmer_id,
                crop_id,
                quantity,
                unit,
            )

            print("\nCrop yield recorded successfully.")
            print(yield_record.display_info())

        except ValueError as error:
            print(f"\nError: {error}")

    def view_farmer(self):
        """Display a farmer by ID."""
        print("\n--- View Farmer ---")

        farmer_id = self._read_id("Enter farmer ID: ")
        farmer = self.farmer_service.get_farmer(farmer_id)

        if farmer is None:
            print("\nFarmer not found.")
            return

        print("\n" + farmer.display_info())

    def view_all_farmers(self):
        """Display all registered farmers."""
        print("\n--- All Farmers ---")

        farmers = self.farmer_service.get_all_farmers()

        if not farmers:
            print("\nNo farmers found.")
            return

        for farmer in farmers.values():
            print("\n" + farmer.display_info())
            print("-" * 40)

    def view_crop(self):
        """Display a crop by ID."""
        print("\n--- View Crop ---")

        crop_id = self._read_id("Enter crop ID: ")
        crop = self.crop_service.get_crop(crop_id)

        if crop is None:
            print("\nCrop not found.")
            return

        print("\n" + crop.display_info())

    def view_all_crops(self):
        """Display all registered crops."""
        print("\n--- All Crops ---")

        crops = self.crop_service.get_all_crops()

        if not crops:
            print("\nNo crops found.")
            return

        for crop in crops.values():
            print("\n" + crop.display_info())
            print("-" * 40)

    def view_yield_record(self):
        """Display a yield record with its crop details."""
        print("\n--- View Yield Record ---")

        yield_record_id = self._read_id(
            "Enter yield record ID: "
        )

        details = (
            self.yield_record_service.get_yield_record_details(
                yield_record_id
            )
        )

        if details is None:
            print("\nYield record not found.")
            return

        yield_record = details["yield_record"]
        crop = details["crop"]

        print(
            f"\nYield Record ID: {yield_record.yield_record_id}\n"
            f"Farmer ID: {yield_record.farmer_id}\n"
            f"Crop ID: {yield_record.crop_id}\n"
            f"Crop: {crop.name}\n"
            f"Lifecycle: {crop.lifecycle}\n"
            f"Quantity: {yield_record.quantity}\n"
            f"Unit: {yield_record.unit}"
        )

    def view_all_yield_records(self):
        """Display all yield records with their crop details."""
        print("\n--- All Yield Records ---")

        details = (
            self.yield_record_service
            .get_all_yield_record_details()
        )

        if not details:
            print("\nNo yield records found.")
            return

        for record_details in details.values():
            yield_record = record_details["yield_record"]
            crop = record_details["crop"]

            print(
                f"\nYield Record ID: {yield_record.yield_record_id}\n"
                f"Farmer ID: {yield_record.farmer_id}\n"
                f"Crop ID: {yield_record.crop_id}\n"
                f"Crop: {crop.name}\n"
                f"Lifecycle: {crop.lifecycle}\n"
                f"Quantity: {yield_record.quantity}\n"
                f"Unit: {yield_record.unit}"
            )

            print("-" * 40)

    def update_yield_quantity(self):
        """Update the quantity of an existing yield record."""
        print("\n--- Update Yield Quantity ---")

        yield_record_id = self._read_id(
            "Enter yield record ID: "
        )

        try:
            quantity = float(
                input("Enter new yield quantity: ").strip()
            )
        except ValueError:
            print("\nInvalid quantity.")
            return

        try:
            yield_record = (
                self.yield_record_service.update_quantity(
                    yield_record_id,
                    quantity,
                )
            )

            print("\nYield quantity updated successfully.")
            print(yield_record.display_info())

        except ValueError as error:
            print(f"\nError: {error}")

    @staticmethod
    def _read_id(prompt):
        """Read and validate a positive integer ID."""
        try:
            value = int(input(prompt).strip())

            if value <= 0:
                raise ValueError

            return value

        except ValueError:
            raise ValueError("ID must be a positive integer.")