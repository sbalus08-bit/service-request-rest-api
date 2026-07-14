# Service Request REST API

A simple REST API built with **Python**, **Flask**, and **SQLite** that demonstrates how to retrieve service request information from a database and return it as JSON.

This project was created as a portfolio piece to demonstrate backend development fundamentals, including REST API design, SQLite database integration, Docker containerisation, and version control Git.

___

## Features

 - REST API built using Flask
 - SQLite database for data storage
 - Automatic database and table creation on first run
 - Sample service request data inserted automatically.
 - JSON responses
 - HTTP 404 responses for invalid service request IDs
 - Docker support
 - Clean and lightweight project structure

---

## Technologies used

 - Python 3
 - Flask
 - SQLite
 - Docker
 - Git & GitHub

---

## Project Structure

```text

.
├── app.py
├── database.py
├── Dockerfile
├── requirements.txt
└── .gitignore
```

---

## Running the Project

Create a virtual environment and install the dependencies:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run the application:

python app.py

The API will be available at:

http://localhost:5000/api/service-request/1

Example Response

{
	"id": 1,
	"description": "Replace ATM receipt printer",
	"customer_name": "Adam Johnson",
	"customer_email": "adam.johson
}

Author

Stephan Balus

GitHub: https://github.com/sbalus08-bit
