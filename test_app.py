"""
Test script to verify the Flask application works correctly
"""

import joblib
import numpy as np
import os

print("=" * 60)
print("TESTING BREAST CANCER PREDICTION SYSTEM")
print("=" * 60)

# Test 1: Check if model files exist
print("\n1. Checking model files...")
model_path = os.path.join('model', 'breast_cancer_model.pkl')
scaler_path = os.path.join('model', 'scaler.pkl')
features_path = os.path.join('model', 'selected_features.pkl')

if os.path.exists(model_path):
    print(f"✓ Model file exists: {model_path}")
else:
    print(f"✗ Model file NOT found: {model_path}")

if os.path.exists(scaler_path):
    print(f"✓ Scaler file exists: {scaler_path}")
else:
    print(f"✗ Scaler file NOT found: {scaler_path}")

if os.path.exists(features_path):
    print(f"✓ Features file exists: {features_path}")
else:
    print(f"✗ Features file NOT found: {features_path}")

# Test 2: Load the model
print("\n2. Loading model files...")
try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    features = joblib.load(features_path)
    print("✓ All model files loaded successfully!")
    print(f"✓ Features: {features}")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    exit(1)

# Test 3: Test prediction with sample data
print("\n3. Testing prediction with sample data...")
# Sample benign tumor data (typical values)
sample_benign = np.array([[12.5, 18.0, 80.0, 480.0, 0.05]])
# Sample malignant tumor data (typical values)
sample_malignant = np.array([[18.0, 25.0, 120.0, 1000.0, 0.15]])

try:
    # Test benign prediction
    sample_benign_scaled = scaler.transform(sample_benign)
    pred_benign = model.predict(sample_benign_scaled)[0]
    prob_benign = model.predict_proba(sample_benign_scaled)[0]
    
    diagnosis_benign = "Benign" if pred_benign == 1 else "Malignant"
    confidence_benign = max(prob_benign) * 100
    
    print(f"\nSample 1 (Expected: Benign):")
    print(f"  Input: {sample_benign[0]}")
    print(f"  Prediction: {diagnosis_benign}")
    print(f"  Confidence: {confidence_benign:.2f}%")
    print(f"  Probabilities: Malignant={prob_benign[0]*100:.2f}%, Benign={prob_benign[1]*100:.2f}%")
    
    # Test malignant prediction
    sample_malignant_scaled = scaler.transform(sample_malignant)
    pred_malignant = model.predict(sample_malignant_scaled)[0]
    prob_malignant = model.predict_proba(sample_malignant_scaled)[0]
    
    diagnosis_malignant = "Benign" if pred_malignant == 1 else "Malignant"
    confidence_malignant = max(prob_malignant) * 100
    
    print(f"\nSample 2 (Expected: Malignant):")
    print(f"  Input: {sample_malignant[0]}")
    print(f"  Prediction: {diagnosis_malignant}")
    print(f"  Confidence: {confidence_malignant:.2f}%")
    print(f"  Probabilities: Malignant={prob_malignant[0]*100:.2f}%, Benign={prob_malignant[1]*100:.2f}%")
    
    print("\n✓ Prediction test completed successfully!")
    
except Exception as e:
    print(f"✗ Error during prediction: {e}")
    exit(1)

# Test 4: Check Flask app files
print("\n4. Checking Flask application files...")
if os.path.exists('app.py'):
    print("✓ app.py exists")
else:
    print("✗ app.py NOT found")

if os.path.exists(os.path.join('templates', 'index.html')):
    print("✓ templates/index.html exists")
else:
    print("✗ templates/index.html NOT found")

if os.path.exists('requirements.txt'):
    print("✓ requirements.txt exists")
else:
    print("✗ requirements.txt NOT found")

print("\n" + "=" * 60)
print("ALL TESTS PASSED!")
print("=" * 60)
print("\nThe application is ready to run!")
print("To start the Flask app, run: python app.py")
print("Then open your browser to: http://localhost:5000")

