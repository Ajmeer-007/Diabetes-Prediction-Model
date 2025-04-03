from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Check if model file exists
model_path = 'model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file '{model_path}' not found.")

# Load Model
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(f"Received data: {data}")

    # Validate JSON keys
    required_keys = {'pregnancies', 'glucose', 'bp', 'st', 'insulin', 'bmi', 'dpf', 'age'}
    missing_keys = required_keys - data.keys()
    if missing_keys:
        return jsonify({'error': f'Missing keys: {list(missing_keys)}'}), 400

    try:
        input_data = np.array([[
            data['pregnancies'], data['glucose'], data['bp'], 
            data['st'], data['insulin'], data['bmi'], 
            data['dpf'], data['age']
        ]], dtype=np.float32)

        # Predict
        prediction = model.predict(input_data)
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': f'Model prediction error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
