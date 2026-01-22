"""
Script to train the breast cancer prediction model
This script replicates the Jupyter notebook functionality
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("BREAST CANCER PREDICTION MODEL TRAINING")
print("Student: Onipede Toluwani | Matric No: 22CG031936")
print("=" * 60)

# 1. Load the Breast Cancer Wisconsin Dataset
print("\n1. Loading dataset...")
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['diagnosis'] = data.target

print(f"Dataset Shape: {df.shape}")
print(f"Features: {data.feature_names[:5]}...")

# 2. Check for missing values
print("\n2. Checking for missing values...")
missing = df.isnull().sum().sum()
print(f"Total missing values: {missing}")

# 3. Check target distribution
print("\n3. Target Distribution:")
print(df['diagnosis'].value_counts())
print("(0 = Malignant, 1 = Benign)")

# 4. Feature Selection
print("\n4. Selecting features...")
selected_features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean concavity']
print(f"Selected features: {selected_features}")

X = df[selected_features]
y = df['diagnosis']

# 5. Split Data
print("\n5. Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

# 6. Feature Scaling
print("\n6. Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Feature scaling completed!")

# 7. Model Training
print("\n7. Training Logistic Regression model...")
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train_scaled, y_train)
print("Model training completed!")

# 8. Model Evaluation
print("\n8. Evaluating model...")
y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL EVALUATION METRICS")
print("=" * 60)
print(f"Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"Precision: {precision:.4f} ({precision*100:.2f}%)")
print(f"Recall:    {recall:.4f} ({recall*100:.2f}%)")
print(f"F1-Score:  {f1:.4f} ({f1*100:.2f}%)")
print("=" * 60)

print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Malignant', 'Benign']))

cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)
print(f"\nTrue Negatives (Malignant correctly predicted): {cm[0][0]}")
print(f"False Positives (Malignant predicted as Benign): {cm[0][1]}")
print(f"False Negatives (Benign predicted as Malignant): {cm[1][0]}")
print(f"True Positives (Benign correctly predicted): {cm[1][1]}")

# 9. Save the Model
print("\n9. Saving model files...")
model_dir = 'model'
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

joblib.dump(model, os.path.join(model_dir, 'breast_cancer_model.pkl'))
joblib.dump(scaler, os.path.join(model_dir, 'scaler.pkl'))
joblib.dump(selected_features, os.path.join(model_dir, 'selected_features.pkl'))

print(f"✓ Model saved to {os.path.join(model_dir, 'breast_cancer_model.pkl')}")
print(f"✓ Scaler saved to {os.path.join(model_dir, 'scaler.pkl')}")
print(f"✓ Features saved to {os.path.join(model_dir, 'selected_features.pkl')}")

# 10. Test Model Loading
print("\n10. Testing model loading...")
loaded_model = joblib.load(os.path.join(model_dir, 'breast_cancer_model.pkl'))
loaded_scaler = joblib.load(os.path.join(model_dir, 'scaler.pkl'))
loaded_features = joblib.load(os.path.join(model_dir, 'selected_features.pkl'))

print("✓ Model loaded successfully!")
print(f"✓ Loaded features: {loaded_features}")

# Test prediction with sample data
sample_data = X_test.iloc[0:3]
sample_scaled = loaded_scaler.transform(sample_data)
predictions = loaded_model.predict(sample_scaled)
prediction_proba = loaded_model.predict_proba(sample_scaled)

print("\n11. Testing predictions with sample data:")
for i, (pred, proba) in enumerate(zip(predictions, prediction_proba)):
    diagnosis = "Benign" if pred == 1 else "Malignant"
    confidence = max(proba) * 100
    actual = "Benign" if y_test.iloc[i] == 1 else "Malignant"
    print(f"Sample {i+1}: Predicted={diagnosis} (Confidence: {confidence:.2f}%), Actual={actual}")

print("\n" + "=" * 60)
print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
print("=" * 60)
print("\nYou can now run the Flask application using: python app.py")

