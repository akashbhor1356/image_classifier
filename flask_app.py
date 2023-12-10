from flask import Flask, request, jsonify
from torchvision import models, transforms
from PIL import Image
import torch
import numpy as np

app = Flask(__name__)

# Load the saved model
model = models.resnet18(pretrained=True)
# ... (Rest of your model setup code)

# Define transformations for incoming images
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Route for predicting classes
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file found'})
    
    file = request.files['file']
    
    # Ensure the file is an image
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    
    if file:
        try:
            image = Image.open(file.stream)
            input_tensor = preprocess(image)
            input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension
            
            # Make predictions
            outputs = model(input_batch)
            _, preds = torch.max(outputs, 1)
            
            predicted_class = preds.item()  # Get the predicted class index
            class_names = ['daisy', 'dandelion']  # Define your class names here
            
            predicted_class_name = class_names[predicted_class]
            
            return jsonify({'predicted_class': predicted_class_name})
        except Exception as e:
            return jsonify({'error': str(e)})
    return jsonify({'error': 'Invalid file'})

if __name__ == '__main__':
    app.run(debug=True)
