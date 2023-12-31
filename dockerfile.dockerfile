# Use an official PyTorch image as the base image
FROM pytorch/pytorch:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script containing your code into the container
COPY flask_app.py /app/flask_app.py

# Install any necessary dependencies (if not already installed in the base image)
RUN pip install torchvision matplotlib pillow

# Set the command to run your script when the container starts
CMD ["python", "flask_app.py"]
