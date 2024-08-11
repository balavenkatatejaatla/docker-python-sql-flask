# Use an official Ubuntu base image
FROM ubuntu:22.04

# Set environment variables to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install necessary packages
RUN apt-get update -y && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    unixodbc \
    unixodbc-dev \
    curl \
    gnupg \
    software-properties-common && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Set up a Python virtual environment
RUN python3 -m venv /opt/myenv

# Activate the virtual environment and install dependencies
COPY requirements.txt /opt/
RUN /opt/myenv/bin/pip install --upgrade pip && \
    /opt/myenv/bin/pip install -r /opt/requirements.txt

# Copy your Flask application into the Docker image
COPY test.py /opt/

# Set the environment variable to use the virtual environment
ENV PATH="/opt/myenv/bin:$PATH"

# Set the working directory
WORKDIR /opt

# Expose port 80
EXPOSE 80

# Run your Flask application
CMD ["python", "test.py"]

