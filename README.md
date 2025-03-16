# Cloud-Based API Testing Framework

A Python-based framework for automated API testing, containerized with Docker and integrated with a continuous integration (CI/CD) pipeline. This framework includes data-driven testing, cloud deployment

## Table of Contents
1. [Overview](#overview)  
2. [Project Structure](#project-structure)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Usage](#usage)  

---

## Overview
This project aims to simplify and automate the testing of RESTful APIs. It uses:
- **Requests** for making HTTP calls.
- **Pytest** for structuring and running tests.
- **Data-Driven Testing** using CSV/JSON files (planned for upcoming days).
- **Docker** for containerization and consistent deployment

### Key Features
- Automated test cases for GET, POST, PUT, DELETE endpoints.
- Assertions on response status, headers, and body.
- Continuous Integration (CI) with GitHub Actions, Jenkins, or CircleCI (to be configured).
- Scalable, cloud-based execution and reporting tools.

---

## Project Structure
The project structure is as follows:

````````````
project-root/
  ├─ tests/
  │  └─ test_api_endpoints.py   # Contains your pytest test cases
  ├─ data/
  │  └─ test_data.json           # (Example) Data files for test cases
  ├─ endpoints/
  │  └─ endpoint_factory.py      # Factory pattern for API test
  │  └─ api_endpoint.py          # Page Object pattern for API test
  ├─ requirements.txt
  ├─ Jenkinsfile
  ├─ Dockerfile
  ├─ README.md
  └─ ...
````````````

| Folder/File        | Description                                               |
|--------------------|-----------------------------------------------------------|
| `tests/`           | Holds all test files and supporting modules.             |
| `data/`            | Stores CSV/JSON files for data-driven testing.           |
| `endpoints/`       | Hosts the Factory and Page Object Model for API testing  |
| `requirements.txt` | Lists Python dependencies for the project.               |
| `Dockerfile`       | Instructions to containerize the application.            |
| `Jenkinsfile`      | Jenkins Instruction files for CI/CD.                     |
| `README.md`        | Project documentation (this file).                       |

---

## Prerequisites
- **Python 3.8+**  
  Make sure Python is installed:  
  ````````````bash
  python --version
  ````````````
- **Git**  
  Required for cloning the repository and version control.
- **Docker** (essential for containerizing).  
  ````````````bash
  docker --version
  ````````````

---

## Installation

1. **Clone the Repository**  
   ````````````bash
   git clone https://github.com/wilsontu/PyAPI-CloudTest.git
   cd PYAPI-CLOUDTEST
   ````````````

2. **Create & Activate a Virtual Environment**  
   ````````````bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate     # On Windows
   ````````````

3. **Install Dependencies**  
   ````````````bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ````````````

---

## Usage

1. **Add/Update Test Cases**
   - Write or update tests in the `tests/` directory.
   - Each test file should follow the `pytest` naming convention (e.g., `test_*.py`).

2. **Run Tests**  
   ````````````bash
   pytest --maxfail=1 --disable-warnings -v
   ````````````
   - **`--maxfail=1`** stops the run on the first failure (optional).
   - **`-v`** increases verbosity.

3. **View Test Reports**
   - For now, your results are visible in the console.
   - In the future, will possibly add a dashboard (Flask or Django) will visualize results more neatly.

---

