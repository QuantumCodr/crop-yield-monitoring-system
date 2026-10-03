# Crop Yield Monitoring System

## Overview

The Crop Yield Monitoring System is a Python-based Object-Oriented Programming project developed to demonstrate how software can be used to monitor crop production information.

The system allows farmers and crop information to be registered and allows crop yield records to be created, viewed, and updated.

The project was developed as part of the PROG211 Object-Oriented Programming 1 individual assignment.

## Problem

Farmers produce different crops during different farming seasons and need to keep records of their production.

Without an organized system, crop and production information can become difficult to manage and monitor.

This project provides a simple system for recording:

- Farmer information
- Crop information
- Crop yield information

## Objectives

The system aims to:

- Register farmers.
- Register supported crops.
- Record crop yield information.
- View individual farmer records.
- View all registered farmers.
- View individual crop records.
- View all registered crops.
- View individual yield records.
- View all yield records.
- Update recorded yield quantities.
- Demonstrate Object-Oriented Programming concepts.

## Main Features

### Farmer Management

The system allows users to:

- Register a farmer.
- View a farmer by ID.
- View all registered farmers.

### Crop Management

The system allows users to:

- Register a crop.
- View a crop by ID.
- View all registered crops.
- Validate supported crop types.

### Yield Monitoring

The system allows users to:

- Record crop yield.
- View a yield record.
- View all yield records.
- Update a yield quantity.
- Associate a yield record with an existing farmer and crop.

## Supported Crop Types

The system currently supports:

- Rice
- Cassava
- Maize
- Groundnut
- Vegetable
- Other

## Object Relationships

The system uses three main classes:

```text
Farmer
   ↓ grows
Crop
   ↓ produces
YieldRecord

A YieldRecord connects a farmer with a crop and records the quantity produced.

Object-Oriented Programming Design
Farmer

The Farmer class represents a farmer in the system.

Attributes:

farmer_id
name
location

Methods:

display_info()
Crop

The Crop class represents a crop being monitored.

Attributes:

crop_id
name
season

Methods:

display_info()
create_basic()
is_valid_crop()

The project demonstrates:

Instance method through display_info()
Class method through create_basic()
Static method through is_valid_crop()
YieldRecord

The YieldRecord class represents crop production information.

Attributes:

yield_record_id
farmer_id
crop_id
quantity
unit

Methods:

display_info()
update_quantity()
Data Structure

The project uses one main data structure: a dictionary.

Multiple records are stored using their unique IDs as dictionary keys.

Example:

{
    "1": {
        "farmer_id": 1,
        "name": "Mohamed Kamara",
        "location": "Waterloo"
    }
}

This structure is used for farmers, crops, and yield records.

Data Persistence

The system uses JSON files to store information:

data/
├── farmers.json
├── crops.json
└── yield_records.json

The repository layer handles reading and writing the JSON files.

System Architecture

The project uses a simple layered structure:

User
  ↓
CLI
  ↓
Services
  ↓
Repositories
  ↓
JSON Data
Models

The model layer contains the main domain classes.

app/models/
├── farmer.py
├── crop.py
└── yield_record.py
Repositories

The repository layer handles JSON persistence.

app/repositories/
├── farmer_repository.py
├── crop_repository.py
└── yield_record_repository.py
Services

The service layer contains application and validation logic.

app/services/
├── farmer_service.py
├── crop_service.py
└── yield_record_service.py
CLI

The CLI layer handles user interaction.

app/cli/
├── application.py
├── menu.py
└── handlers.py
Project Structure
crop-yield-monitoring-system/
│
├── README.md
├── main.py
│
├── app/
│   ├── __init__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── farmer.py
│   │   ├── crop.py
│   │   └── yield_record.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── farmer_repository.py
│   │   ├── crop_repository.py
│   │   └── yield_record_repository.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── farmer_service.py
│   │   ├── crop_service.py
│   │   └── yield_record_service.py
│   │
│   └── cli/
│       ├── __init__.py
│       ├── application.py
│       ├── menu.py
│       └── handlers.py
│
├── data/
│   ├── farmers.json
│   ├── crops.json
│   └── yield_records.json
│
└── docs/
    └── report.md
Validation

The system performs basic validation including:

Farmer names cannot be empty.
Farmer locations cannot be empty.
Crop names must be supported.
Farming seasons cannot be empty.
Farmer IDs must exist before recording yield.
Crop IDs must exist before recording yield.
Yield quantities must be greater than zero.
Yield units cannot be empty.
Record IDs must be positive integers.
DPG Alignment
Open Source

The project is maintained as source code in a GitHub repository so that the implementation and documentation can be accessed and reviewed.

Inclusion and Accessibility

The system uses a simple command-line interface with clear numbered options and readable text.

Privacy

The project uses basic demonstration information and does not require sensitive personal information.

Modularity and Reusability

The system separates models, repositories, services, and CLI components.

This makes the code easier to understand, maintain, and reuse.

Example Usage
View All Farmers
--- All Farmers ---

Farmer ID: 1
Name: Mohamed Kamara
Location: Waterloo
----------------------------------------

Farmer ID: 2
Name: Mariama Sesay
Location: Makeni
----------------------------------------
Record Crop Yield
--- Record Crop Yield ---

Enter farmer ID: 1
Enter crop ID: 1
Enter yield quantity: 2500
Enter unit (kg, tonnes, etc.): kg

Crop yield recorded successfully.
Yield Record ID: 1
Update Yield Quantity
--- Update Yield Quantity ---

Enter yield record ID: 1
Enter new yield quantity: 3000

Yield quantity updated successfully.
How to Run

Make sure Python is installed.

From the project directory, run:

py main.py

The application will display the main menu.

Main Menu
==================================================
        CROP YIELD MONITORING SYSTEM
==================================================
1. Register Farmer
2. Register Crop
3. Record Crop Yield
4. View Farmer
5. View All Farmers
6. View Crop
7. View All Crops
8. View Yield Record
9. View All Yield Records
10. Update Yield Quantity
0. Exit
==================================================
Author

QuantumCodr

Python
Object-Oriented Programming 1
Limkokwing University of Creative Technology, Sierra Leone

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.