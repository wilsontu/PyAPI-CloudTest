# Cloud-Based API Testing Framework

A Python-based framework for automated API testing, containerized with Docker and integrated with a continuous integration (CI/CD) pipeline. This framework includes data-driven testing, cloud deployment, and a web dashboard for monitoring test results and metrics.

## Table of Contents
1. [Overview](#overview)  
2. [Project Structure](#project-structure)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Roadmap](#roadmap) 

---

## Overview
This project aims to simplify and automate the testing of RESTful APIs. It uses:
- **Requests** for making HTTP calls.
- **Pytest** for structuring and running tests.
- **Data-Driven Testing** using CSV/JSON files (planned for upcoming days).
- **Flask** (or Django) for a basic dashboard to visualize test results (in later phases).
- **Docker** for containerization and consistent deployment.
- **Cloud deployment** (AWS, GCP, or Azure) to run these tests at scale.

### Key Features
- Automated test cases for GET, POST, PUT, DELETE endpoints.
- Assertions on response status, headers, and body.
- Continuous Integration (CI) with GitHub Actions, Jenkins, or CircleCI (to be configured).
- Scalable, cloud-based execution and reporting tools.

---

## Project Structure
A recommended project structure is as follows:

````````````
project-root/
  ├─ tests/
  │  └─ test_api_endpoints.py   # Contains your pytest test cases
  ├─ data/
  │  └─ test_data.csv           # (Example) Data files for test cases
  ├─ dashboard/                 # Flask or Django app for displaying results
  ├─ requirements.txt
  ├─ Dockerfile
  ├─ README.md
  └─ ...
````````````

| Folder/File        | Description                                               |
|--------------------|-----------------------------------------------------------|
| `tests/`           | Holds all test files and supporting modules.             |
| `data/`            | Stores CSV/JSON files for data-driven testing.           |
| `dashboard/`       | Hosts the web framework code (Flask or Django).          |
| `requirements.txt` | Lists Python dependencies for the project.               |
| `Dockerfile`       | Instructions to containerize the application.            |
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
- **Docker** (optional for Day 1, essential for containerizing later).  
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
   - In the future, a dashboard (Flask or Django) will visualize results more neatly.

---

## Roadmap

1. **Test Scripting (Day 2–3)**  
   - Write basic API test cases for GET, POST, PUT, DELETE.  
   - Introduce data-driven testing with CSV/JSON.

2. **Containerization & CI/CD (Day 4–5)**  
   - Create a Dockerfile to containerize the tests.  
   - Set up CI/CD pipelines to run tests on every commit.

3. **Dashboard & Cloud Setup (Day 6–7)**  
   - Develop a Flask or Django app to display test results.  
   - Deploy container to AWS/GCP/Azure and configure an API gateway.

4. **Monitoring, Logging & Alerts (Day 8)**  
   - Integrate logging to a cloud database.  
   - Set up alerts via email or Slack when tests fail.

5. **Load Testing & Security (Day 9)**  
   - Conduct load tests with Locust or JMeter.  
   - Review security best practices and ensure compliance.

6. **Final Integration & Documentation (Day 10–14)**  
   - Comprehensive testing, bug fixes, final documentation, and handover.

---
