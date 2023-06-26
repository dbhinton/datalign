# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the entire backend directory into the container
COPY ./backend/requirements.txt /app/backend/requirements.txt

# Install any dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy the backend code into the container
COPY ./backend /app/backend

# Set the command to run the Flask application
CMD python app.py
