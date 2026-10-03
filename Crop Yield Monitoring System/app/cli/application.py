"""
------------------------------------------------------------
Program Name : Crop Yield Monitoring System
Author       : QuantumCodr
Date         : 2026-10-02
Language     : Python
Module       : CLI Application
Description  : Controls the main application loop and
               connects menu choices to CLI handlers.
------------------------------------------------------------
"""

from app.cli.handlers import CLIHandlers
from app.cli.menu import display_menu


class Application:
    """Controls the command-line application."""

    def __init__(
        self,
        farmer_service,
        crop_service,
        yield_record_service
    ):
        self.handlers = CLIHandlers(
            farmer_service,
            crop_service,
            yield_record_service
        )

    def run(self):
        """Start and maintain the application loop."""
        while True:
            display_menu()

            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.handlers.register_farmer()

            elif choice == "2":
                self.handlers.register_crop()

            elif choice == "3":
                self.handlers.record_crop_yield()

            elif choice == "4":
                self.handlers.view_farmer()

            elif choice == "5":
                self.handlers.view_all_farmers()

            elif choice == "6":
                self.handlers.view_crop()

            elif choice == "7":
                self.handlers.view_all_crops()

            elif choice == "8":
                self.handlers.view_yield_record()

            elif choice == "9":
                self.handlers.view_all_yield_records()

            elif choice == "10":
                self.handlers.update_yield_quantity()

            elif choice == "0":
                print(
                    "\nThank you for using the "
                    "Crop Yield Monitoring System."
                )
                break

            else:
                print("\nInvalid choice. Please try again.")