from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="prediction_logs"
)
cursor = db.cursor()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Perform prediction using the trained model
    # prediction = model.predict(data)
    
    # Log prediction into MySQL database
    cursor.execute("INSERT INTO predictions (input_data, prediction) VALUES (%s, %s)", (str(data), str(prediction)))
    db.commit()
    
    return "Prediction logged successfully"

if __name__ == '__main__':
    app.run(debug=True)
