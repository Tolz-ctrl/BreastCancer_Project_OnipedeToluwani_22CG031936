# Deployment Guide

This guide provides step-by-step instructions for deploying the Breast Cancer Prediction System to various platforms.

## Option 1: Deploy to Render.com (Recommended)

### Prerequisites
- GitHub account
- Render.com account (free tier available)

### Steps

1. **Push your code to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create a new Web Service on Render**
   - Go to https://render.com
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository: `BreastCancer_Project_OnipedeToluwani_22CG031936`

3. **Configure the service**
   - **Name:** breast-cancer-prediction-toluwani
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt && python train_model.py`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete (5-10 minutes)
   - Your app will be available at: `https://breast-cancer-prediction-toluwani.onrender.com`

## Option 2: Deploy to PythonAnywhere

### Steps

1. **Sign up at PythonAnywhere**
   - Go to https://www.pythonanywhere.com
   - Create a free account

2. **Upload your files**
   - Go to "Files" tab
   - Upload all project files or clone from GitHub

3. **Install dependencies**
   - Open a Bash console
   - Navigate to your project directory
   - Run: `pip install --user -r requirements.txt`
   - Run: `python train_model.py`

4. **Configure Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Flask"
   - Set the path to your `app.py` file
   - Configure WSGI file to point to your app

5. **Reload and test**
   - Click "Reload" button
   - Visit your app at: `https://yourusername.pythonanywhere.com`

## Option 3: Deploy to Streamlit Cloud

Note: This requires converting the Flask app to Streamlit. Here's a quick Streamlit version:

### Create streamlit_app.py

```python
import streamlit as st
import joblib
import numpy as np
import os

st.set_page_config(page_title="Breast Cancer Prediction", page_icon="🎗️")

# Load model
@st.cache_resource
def load_model():
    model = joblib.load('model/breast_cancer_model.pkl')
    scaler = joblib.load('model/scaler.pkl')
    features = joblib.load('model/selected_features.pkl')
    return model, scaler, features

model, scaler, features = load_model()

st.title("🎗️ Breast Cancer Prediction System")
st.write("**Student:** Onipede Toluwani | **Matric No:** 22CG031936")

st.warning("⚠️ Educational Purpose Only: This system is strictly for educational purposes.")

st.header("Enter Tumor Features")

# Input fields
radius = st.number_input("Mean Radius", min_value=0.0, value=14.5, step=0.1)
texture = st.number_input("Mean Texture", min_value=0.0, value=19.8, step=0.1)
perimeter = st.number_input("Mean Perimeter", min_value=0.0, value=92.3, step=0.1)
area = st.number_input("Mean Area", min_value=0.0, value=654.8, step=1.0)
concavity = st.number_input("Mean Concavity", min_value=0.0, value=0.1234, step=0.0001, format="%.4f")

if st.button("🔍 Predict"):
    # Prepare input
    input_data = np.array([[radius, texture, perimeter, area, concavity]])
    input_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    proba = model.predict_proba(input_scaled)[0]
    
    diagnosis = "Benign" if prediction == 1 else "Malignant"
    confidence = max(proba) * 100
    
    # Display result
    if diagnosis == "Benign":
        st.success(f"### Prediction: {diagnosis}")
    else:
        st.error(f"### Prediction: {diagnosis}")
    
    st.write(f"**Confidence:** {confidence:.2f}%")
    st.write(f"**Probability of Malignant:** {proba[0]*100:.2f}%")
    st.write(f"**Probability of Benign:** {proba[1]*100:.2f}%")
```

### Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Click "New app"
4. Select your repository
5. Set main file to `streamlit_app.py`
6. Click "Deploy"

## Testing Your Deployment

After deployment, test with these sample values:

### Benign Sample
- Mean Radius: 12.5
- Mean Texture: 18.0
- Mean Perimeter: 80.0
- Mean Area: 480.0
- Mean Concavity: 0.05

### Malignant Sample
- Mean Radius: 18.0
- Mean Texture: 25.0
- Mean Perimeter: 120.0
- Mean Area: 1000.0
- Mean Concavity: 0.15

## Troubleshooting

### Model files not found
- Ensure you run `python train_model.py` before starting the app
- Check that model files are in the `model/` directory

### Port issues
- Render and PythonAnywhere handle ports automatically
- For local testing, use port 5000

### Dependencies not installing
- Check Python version compatibility
- Ensure requirements.txt is in the root directory

## Update BreastCancer_hosted_webGUI_link.txt

After successful deployment, update the file with your live URL:

```
Name: Onipede Toluwani
Matric Number: 22CG031936
Machine Learning Algorithm Used: Logistic Regression
Model Persistence Method Used: Joblib
Live URL of the Hosted Application: [YOUR_DEPLOYED_URL_HERE]
GitHub Repository Link: https://github.com/Tolz-ctrl/BreastCancer_Project_OnipedeToluwani_22CG031936.git
```

