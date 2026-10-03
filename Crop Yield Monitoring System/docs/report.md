
```markdown
# CROP YIELD MONITORING SYSTEM

## PROG211 – OBJECT-ORIENTED PROGRAMMING 1

### Individual Assignment

**Project:** Crop Yield Monitoring System  
**Domain:** Agriculture  
**Author:** QuantumCodr  
**Language:** Python  
**Date:** 2026-10-02

---

# 1. Introduction

The Crop Yield Monitoring System is a Python-based application developed to demonstrate Object-Oriented Programming concepts through a real-world agriculture problem.

The system provides a simple way to register farmers, register crops, record crop production, view production records, and update yield quantities.

The project uses Python classes and objects together with a dictionary-based data structure and JSON persistence.

---

# 2. Problem Statement

Farmers produce different crops across different farming seasons and need to maintain accurate records of their production.

When production information is handled manually, it can become difficult to organize and retrieve.

The Crop Yield Monitoring System provides a simple computerized approach for storing and monitoring farmer, crop, and yield information.

---

# 3. Objectives

The objectives of the system are to:

- Register farmers.
- Register crops.
- Record crop yields.
- View individual farmer information.
- View all farmers.
- View individual crop information.
- View all crops.
- View individual yield records.
- View all yield records.
- Update yield quantities.
- Demonstrate Object-Oriented Programming concepts.

---

# 4. System Design

The system contains three main classes:

### Farmer

Represents a farmer participating in crop production.

Attributes:

- Farmer ID
- Name
- Location

### Crop

Represents a crop being monitored.

Attributes:

- Crop ID
- Name
- Season

### YieldRecord

Represents the production result associated with a farmer and crop.

Attributes:

- Yield Record ID
- Farmer ID
- Crop ID
- Quantity
- Unit

The relationship between the classes is:

```text
Farmer
   ↓ grows
Crop
   ↓ produces
YieldRecord
5. Object-Oriented Programming Concepts

The project demonstrates the following OOP concepts.

Classes and Objects

Three classes are implemented:

Farmer
Crop
YieldRecord

Objects are created from these classes when farmers, crops, and yield records are registered.

Attributes

Each class contains attributes representing the information required by the system.

Instance Methods

Instance methods are used to perform operations on individual objects.

Examples include:

display_info()
update_quantity()
Class Method

The Crop class contains:

create_basic()

This class method creates a Crop object using the class itself.

Static Method

The Crop class contains:

is_valid_crop()

This method validates whether a crop type is supported without requiring a Crop object.

6. Data Structure

The system uses one main data structure: a dictionary.

The dictionary uses unique IDs as keys.

Example:

{
    "1": {
        "farmer_id": 1,
        "name": "Mohamed Kamara",
        "location": "Waterloo"
    }
}

The same approach is used for farmers, crops, and yield records.

7. Data Persistence

The system stores information in JSON files:

farmers.json
crops.json
yield_records.json

The repository layer is responsible for reading and writing these files.

This keeps file handling separate from the models and services.

8. System Architecture

The project follows a simple layered structure:

User
  ↓
CLI
  ↓
Services
  ↓
Repositories
  ↓
JSON Files
Models

Responsible for representing system objects.

Repositories

Responsible for JSON storage and retrieval.

Services

Responsible for application rules and validation.

CLI

Responsible for user input, menus, and displaying results.

9. Main Features

The application provides the following operations:

Register Farmer
Register Crop
Record Crop Yield
View Farmer
View All Farmers
View Crop
View All Crops
View Yield Record
View All Yield Records
Update Yield Quantity
Exit
10. Validation

The system performs basic validation to improve the reliability of entered information.

Examples include:

Empty farmer names are rejected.
Empty farmer locations are rejected.
Unsupported crop types are rejected.
Empty farming seasons are rejected.
A yield cannot be recorded for a non-existing farmer.
A yield cannot be recorded for a non-existing crop.
Yield quantity must be greater than zero.
Yield units cannot be empty.
IDs must be positive integers.
11. Example Execution
Viewing all farmers
--- All Farmers ---

Farmer ID: 1
Name: Mohamed Kamara
Location: Waterloo
----------------------------------------

Farmer ID: 2
Name: Mariama Sesay
Location: Makeni
----------------------------------------

Farmer ID: 3
Name: Abdul Rahman
Location: Bo
----------------------------------------
Recording crop yield
--- Record Crop Yield ---

Enter farmer ID: 1
Enter crop ID: 1
Enter yield quantity: 2500
Enter unit (kg, tonnes, etc.): kg

Crop yield recorded successfully.
Yield Record ID: 1
Updating yield
--- Update Yield Quantity ---

Enter yield record ID: 1
Enter new yield quantity: 3000

Yield quantity updated successfully.
12. DPG Alignment
Open Source

The project source code and documentation are maintained in a GitHub repository for review and access.

Inclusion and Accessibility

The command-line interface uses simple numbered options and readable text, making the system straightforward to operate.

Privacy

The system uses basic demonstration information and does not require sensitive personal information.

Modularity

The application separates models, repositories, services, and the CLI.

This makes individual components easier to understand, maintain, and reuse.

13. Project Structure
crop-yield-monitoring-system/
│
├── README.md
├── main.py
│
├── app/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   └── cli/
│
├── data/
│   ├── farmers.json
│   ├── crops.json
│   └── yield_records.json
│
└── docs/
    └── report.md
14. Screenshots
Screenshot 1 – Main Application Menu

[Insert screenshot of the main menu here.]

Screenshot 2 – Farmer and Crop Management

[Insert screenshot showing farmer/crop registration or viewing.]

Screenshot 3 – Crop Yield Recording

[Insert screenshot showing a yield being recorded.]

Screenshot 4 – Yield Monitoring

[Insert screenshot showing yield records and/or quantity update.]

15. GitHub

The complete source code and README are maintained in the project's GitHub repository.

Repository:

https://github.com/QuantumCodr/crop-yield-monitoring-system

16. Conclusion

The Crop Yield Monitoring System demonstrates how Object-Oriented Programming can be applied to a real-world agriculture problem.

The project implements classes, objects, attributes, instance methods, a class method, and a static method. It also uses a dictionary to store multiple objects and JSON files for data persistence.

The separation between models, repositories, services, and the CLI keeps the system organized and makes the implementation easier to understand and maintain.


## Hardcopy formatting

Use the same format we established for the previous assignment:

- **Font:** Tahoma
- **Size:** 10 pt
- **Line spacing:** 1.15
- **Alignment:** Justified
- **Margins:** Normal or approximately 0.75"
- **Title:** Centered and bold
- Keep the report around **3–4 pages including screenshots**.

For screenshots, I'd use **four**:

1. Main menu
2. View All Farmers / View All Crops
3. Record Crop Yield
4. Update Yield Quantity / View All Yield Records

That gives the lecturer visible evidence of the main functionality without filling the report with unnecessary code screenshots.