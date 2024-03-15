# Official Python base image
FROM python:3.9.12-slim-buster

# Set the current working directory to /code
WORKDIR /code

# Copy the requirements.txt file to the /code directory
COPY requirements.txt /code/requirements.txt

# Install the Python packages from the requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the Python scripts to the directory
COPY . /code/app

# Expose the port
EXPOSE 8000:8000

# Start the Python web application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]