# Shipay Back-end Challenge

This project is a solution to the Shipay Back-end Challenge. It includes SQL queries, REST APIs, troubleshooting, code review, and design pattern discussion.

## Table of Contents

- [Installation](#installation)
- [Running Locally](#running-locally)
- [API Endpoints](#api-endpoints)
- [Task1](#Task1)
- [Task2](#Task2)
- [Task3](#Task_3)
- [Task4](#Task_4)
- [Task5](#Task_5)
- [Task6](#Task_6)
- [Task7](#Task_7)
- [Task8](#Task8)

- [Contributing](#contributing)


## Installation

1. Clone the project repository:
```https://github.com/oyugirachel/backend-challenge-shipay```
2. Navigate to the main directory ``cd backend-challenge``
3. Install the required dependencies:
``pip install -r requirements.txt``
4. Configure the database connection in your application settings.


5. Run the Flask application locally:
``python3 app.py``



2. Install the required packages using `pip install Flask SQLAlchemy`.
The API will be accessible locally at `http://127.0.0.1:5000/`.


## Running Locally

2. Run the Flask application using `python3 app.py`.

## Task1: Building an SQL query to retrieve user information.
This implemenation can be found in the ``user_sqlquery.py``



## Task_2: Rewriting the SQL query using an ORM (Flask-SQLAlchemy).
This implementation can be found in the ``models.py``   and further configured and broken down in the ``orm_query.py`` 


## API Endpoints


## Task_3: Creating API to List User's Role by ID
The implementation of the task is found in the ``app.py``
The Endpoint for testing the get ``user_role`` by ``user_id`` is : 

``GET /api/users/{user_id}/role``
[![Screenshot-from-2023-09-25-06-28-57.png](https://i.postimg.cc/SQgtQ5J3/Screenshot-from-2023-09-25-06-28-57.png)](https://postimg.cc/Bt1CMm5B)
``POST /api/role``

[![Screenshot-from-2023-09-25-06-29-17.png](https://i.postimg.cc/SRLSCh36/Screenshot-from-2023-09-25-06-29-17.png)](https://postimg.cc/7J6rrpxh)

## Task_4: Creating API to Create User
Endpoint: ``POST /api/users``
[![Screenshot-from-2023-09-25-06-29-48.png](https://i.postimg.cc/9fXW9KYT/Screenshot-from-2023-09-25-06-29-48.png)](https://postimg.cc/hXwWWCwP)

N/B : Use tools like Postman, insomnia or curl to interact with the REST API.


## Testing with pytest
For testing your code, you can use pytest. Here's a basic structure for your pytest setup:

1. Install pytest: ``pip install pytest``

2. Create a ``tests`` directory in your project.

3. Write test functions for each API endpoint and any other critical parts of your code.

4. Run pytest from the command line in your project's root directory: ``pytest``

5. Ensure all tests pass successfully.

## Task_6: Troubleshooting Log

Based on the log provided, the error seems to be related to the attribute ``WALLET_X_TOKEN_MAX_AGE`` not being found in the ``core.settings`` module. The error message indicates that AttributeError: module ``core.settings`` has no attribute ``WALLET_X_TOKEN_MAX_AGE``.

To resolve this issue, The following should be checked:

Ensure that the ``core.settings`` module exists and is importable.
Verify that the ``WALLET_X_TOKEN_MAX_AGE`` attribute is defined in the ``core.settings`` module.
Make sure that the ``core.settings`` module is correctly imported in the ``tasks.wallet_oauth`` module where it is used.

## Task_7: Code Review
Detailed code review comments can be found in code_review.txt.
The code lacks proper error handling and exception logging. It's recommended to catch exceptions and log them appropriately to aid in debugging and monitoring.

The database connection string is hard-coded. Consider using environment variables or configuration files to manage sensitive information like database credentials.

The ``greetings`` function is a nice touch for console output.

The scheduling logic using ``BlockingScheduler`` seems appropriate for running periodic tasks.

The ``task1`` function is responsible for exporting data to an Excel file. It's well-structured and organized.

## Task_8: Design Patterns for Normalizing Third-Party Services
Design patterns used: The Adapter Pattern
Reasons: The Adapter Pattern allows you to create a common interface that abstracts the differences between various third-party services.

For example, if you are dealing with email services from multiple providers, you can create an EmailService interface with methods like sendEmail and then create specific adapters for each email service provider (e.g., GmailAdapter, OutlookAdapter). Each adapter implements the sendEmail method according to the specific API of the corresponding email service.

This approach allows you to switch between different email service providers without changing the core code of your application. It also promotes code reusability and maintainability.
## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub. 
2. Create a new branch for your feature or bug fix. 
3. Make your changes and commit them. 
4. Push your changes to your fork. 
5. Create a pull request to submit your changes for review.
