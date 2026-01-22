"""
Breast Cancer Prediction System - Web Application
Student: Onipede Toluwani
Matric No: 22CG031936

This Flask application provides a web interface for breast cancer prediction.
"""

from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model, scaler, and feature names
MODEL_PATH = os.path.join('model', 'breast_cancer_model.pkl')
SCALER_PATH = os.path.join('model', 'scaler.pkl')
FEATURES_PATH = os.path.join('model', 'selected_features.pkl')

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    feature_names = joblib.load(FEATURES_PATH)
    print("Model loaded successfully!")
    print(f"Features: {feature_names}")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    scaler = None
    feature_names = None

@app.route('/')
def home():
    """Render the home page with input form"""
    return render_template('index.html', features=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        if model is None or scaler is None:
            return jsonify({
                'error': 'Model not loaded. Please ensure the model files exist in the model directory.'
            }), 500
        
        # Get input data from form
        features = []
        feature_values = {}
        
        for feature in feature_names:
            value = request.form.get(feature)
            if value is None or value == '':
                return jsonify({
                    'error': f'Missing value for {feature}'
                }), 400
            
            try:
                float_value = float(value)
                features.append(float_value)
                feature_values[feature] = float_value
            except ValueError:
                return jsonify({
                    'error': f'Invalid value for {feature}. Please enter a numeric value.'
                }), 400
        
        # Convert to numpy array and reshape
        input_data = np.array(features).reshape(1, -1)
        
        # Scale the input data
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]
        
        # Interpret results
        diagnosis = "Benign" if prediction == 1 else "Malignant"
        confidence = max(prediction_proba) * 100
        
        # Prepare detailed results
        result = {
            'diagnosis': diagnosis,
            'confidence': round(confidence, 2),
            'prediction_value': int(prediction),
            'probabilities': {
                'malignant': round(prediction_proba[0] * 100, 2),
                'benign': round(prediction_proba[1] * 100, 2)
            },
            'input_features': feature_values
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred during prediction: {str(e)}'
        }), 500

@app.route('/api/info', methods=['GET'])
def info():
    """Return information about the model"""
    return jsonify({
        'student_name': 'Onipede Toluwani',
        'matric_number': '22CG031936',
        'algorithm': 'Logistic Regression',
        'persistence_method': 'Joblib',
        'features': feature_names,
        'model_loaded': model is not None
    })

if __name__ == '__main__':
    # Run the Flask app
    # For production deployment, use a production WSGI server like Gunicorn
    app.run(debug=True, host='0.0.0.0', port=5000)

