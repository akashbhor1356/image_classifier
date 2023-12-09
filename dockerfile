# Specify a base image
FROM python:3.9

# Copy and install dependencies for AI model and web service
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy AI model files and web service files into the container
COPY ai_model.py /app/ai_model.py
COPY web_service.py /app/web_service.py

# Set the working directory
WORKDIR /app

# Define how to run the web service
CMD ["python", "web_service.py"]
