# Use a Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set a working directory inside the container
WORKDIR /app

# Copy only the requirements first for efficient caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the project files
COPY . /app/

# By default, the container will run Pytest
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-v", "tests"]
