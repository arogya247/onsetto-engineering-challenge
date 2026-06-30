# Onsetto Engineering Challenge

This repository contains my solution for the **Onsetto Engineering Challenge**, which consists of two parts:

1. **Part 1 – Browser Automation (Playwright)**
2. **Part 2 – Python REST API Client**

Both implementations update a user's banking details and payment method using the provided sandbox account.

---

# Project Structure

```
onsetto-engineering-challenge/
│
├── api/
│   ├── client.py
│   ├── config.py
│   ├── main.py
│   └── __init__.py
│
├── browser/
│   ├── locators.py
│   ├── pages.py
│   ├── main.py
│   └── __init__.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Prerequisites

* Python 3.9+
* pip
* Playwright

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd onsetto-engineering-challenge
```

Create and activate a virtual environment:

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

# Configuration

Create a `.env` file in the project root.

Example:

```env
EMAIL=candidate1@onsetto.test
PASSWORD=Password123!
MFA_CODE=1234
```

---

# Part 1 – Browser Automation

The browser automation is implemented using **Playwright**.

### Workflow

* Navigate to the login page
* Authenticate using the provided credentials
* Complete MFA
* Navigate to the Account page
* Update banking details
* Verify the saved banking information
* Update payment method
* Verify the saved payment information

### Run

```bash
python browser/main.py
```

---

# Part 2 – Python API Client

The API client is implemented using **httpx**.

### Workflow

* Authenticate via `/auth/token`
* Complete MFA using `/auth/mfa/verify`
* Receive a bearer token
* Update banking details
* Update payment method
* Print the masked confirmation returned by the API

### Run

```bash
python api/main.py
```

---

# Technologies Used

* Python
* Playwright
* httpx
* python-dotenv

---

# Error Handling

The API client includes handling for common error scenarios such as:

* Invalid credentials
* Invalid MFA code
* Validation errors
* Rate limiting
* Server errors

The browser automation uses Playwright's built-in assertions to ensure that updates are successfully reflected in the UI.

---

# Design Approach

The project is separated into two independent components:

### Browser Automation

A Page Object Model (POM) structure is used to separate page interactions from the execution logic.

* `pages.py` contains page-specific actions.
* `locators.py` centralizes selectors.
* `main.py` orchestrates the complete workflow.

This structure improves readability and makes the automation easier to maintain.

### API Client

A reusable `APIClient` class encapsulates authentication and API operations, keeping the implementation modular and easy to extend.

---

# Future Improvements

Given additional time, I would consider adding:

* Unit tests and integration tests
* Type checking with `mypy`
* Linting and formatting with `ruff` and `black`
* Structured logging
* Automatic retries with exponential backoff
* GitHub Actions CI pipeline
* Docker support
* A command-line interface (CLI)
* Pydantic models for request and response validation

---

# Notes

This project uses only the sandbox credentials and fake test data provided as part of the engineering challenge. No real banking or payment information is used.

