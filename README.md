# Banking Management System

## Overview
This is a simple **Banking Management System** built using **Python** and **MySQL**. It was developed as a project for the Class 12 Computer Science course. The system allows users to manage bank accounts, perform transactions, and retrieve customer information efficiently.

## Features
- Insert new customer records
- Display sorted records based on:
  - Account Number
  - Customer Name
  - Account Balance
- Search for specific customer details
- Update customer records
- Delete customer records
- Perform transactions:
  - Debit/Withdraw
  - Credit into an account

## Technologies Used
- **Python** (for backend logic)
- **MySQL** (for database management)
- **MySQL Connector** (to connect Python with MySQL)

## Installation
### Prerequisites
Make sure you have the following installed:
- Python 3.x
- MySQL Server
- MySQL Connector for Python

### Steps to Run
1. Clone this repository:
   ```sh
   git clone https://github.com/tapashh/banking-management-system.git
   ```
2. Navigate to the project directory:
   ```sh
   cd banking-management-system
   ```
3. Install dependencies:
   ```sh
   pip install mysql-connector-python
   ```
4. Set up the MySQL database:
   - Open MySQL and create a database:
     ```sql
     CREATE DATABASE BankDB;
     ```
   - Update the database credentials in the Python script if necessary.
5. Run the Python script:
   ```sh
   python bank_management.py
   ```

## Usage
- Follow the on-screen menu to perform different banking operations.
- Ensure MySQL is running before executing the script.

## Contributing
Feel free to fork the repository and submit pull requests if you want to improve the project.

## License
This project is open-source and available under the **MIT License**.

## Author
- **Tapash Biswas**  
  Connect with me on [LinkedIn](https://www.linkedin.com/in/tapash-biswas-783669274/)

---

Enjoy coding! 😊


