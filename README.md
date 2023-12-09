
AI Model Deployment Pipeline
This repository contains code and instructions to set up a simple AI model deployment pipeline using Docker, Kubernetes, and a basic web service.

Task Overview
AI Model Development

Develop a basic image classification model using TensorFlow and the MNIST dataset.
Web Service Creation

Create a Flask-based web service in Python that exposes an API endpoint for predictions and logs results in a MySQL database.
Containerization with Docker

Use Docker to containerize the AI model and the web service.
Deployment with Kubernetes

Deploy the Docker containers using Kubernetes with basic configurations for scaling and managing the application.
Steps to Set Up
Prerequisites
Python (3.7+)
Docker installed
Kubernetes cluster set up (if deploying locally, tools like Minikube or Docker Desktop Kubernetes can be used)
Instructions
AI Model Development

Open ai_model.py and follow the comments to train the image classification model using the MNIST dataset.
Web Service Creation

Ensure Python dependencies are installed using pip install -r requirements.txt.
Configure MySQL connection details in web_service.py.
Run the web service using python web_service.py.
Containerization with Docker

Build the Docker images for the AI model and web service using the provided Dockerfiles.
arduino
Copy code
docker build -t ai-model-image -f Dockerfile .
docker build -t web-service-image -f Dockerfile .
Deployment with Kubernetes

Apply Kubernetes deployment configurations for the AI model and web service.
Copy code
kubectl apply -f ai-model-deployment.yaml
kubectl apply -f web-service-deployment.yaml
Accessing the Application

Once deployed, access the web service API endpoint to make predictions and check the MySQL database for logged results.
