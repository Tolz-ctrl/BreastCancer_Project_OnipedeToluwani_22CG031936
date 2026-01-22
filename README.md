# Breast Cancer Prediction System

**Student:** Onipede Toluwani  
**Matric Number:** 22CG031936  
**Algorithm:** Logistic Regression  
**Model Persistence:** Joblib

## Project Overview

This project implements a Breast Cancer Prediction System using machine learning to predict whether a tumor is benign or malignant based on selected features from the Breast Cancer Wisconsin (Diagnostic) dataset.

**⚠️ DISCLAIMER:** This system is strictly for educational purposes and must not be presented as a medical diagnostic tool.

## Features Used

The model uses the following 5 features:
1. Mean Radius
2. Mean Texture
3. Mean Perimeter
4. Mean Area
5. Mean Concavity

## Model Performance

- **Accuracy:** 92.11%
- **Precision:** 94.37%
- **Recall:** 93.06%
- **F1-Score:** 93.71%

## Project Structure

```
BreastCancer_Project_OnipedeToluwani_22CG031936/
├── app.py                                    # Flask web application
├── requirements.txt                          # Python dependencies
├── train_model.py                           # Script to train the model
├── test_app.py                              # Test script
├── BreastCancer_hosted_webGUI_link.txt     # Deployment information
├── model/
│   ├── model_building.ipynb                # Jupyter notebook for model development
│   ├── breast_cancer_model.pkl             # Trained model
│   ├── scaler.pkl                          # Feature scaler
│   └── selected_features.pkl               # Selected feature names
├── templates/
│   └── index.html                          # Web interface
└── static/
    └── (optional CSS files)
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Tolz-ctrl/BreastCancer_Project_OnipedeToluwani_22CG031936.git
cd BreastCancer_Project_OnipedeToluwani_22CG031936
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Model (if not already trained)

```bash
python train_model.py
```

This will:
- Load the Breast Cancer Wisconsin dataset
- Preprocess the data
- Train a Logistic Regression model
- Save the model files to the `model/` directory
- Display evaluation metrics

### 4. Run the Web Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### 5. Test the Application

```bash
python test_app.py
```

## Using the Web Interface

1. Open your browser to `http://localhost:5000`
2. Enter the tumor feature values:
   - Mean Radius (e.g., 14.5)
   - Mean Texture (e.g., 19.8)
   - Mean Perimeter (e.g., 92.3)
   - Mean Area (e.g., 654.8)
   - Mean Concavity (e.g., 0.1234)
3. Click "Predict" to get the diagnosis
4. The system will display:
   - Prediction (Benign or Malignant)
   - Confidence level
   - Probability breakdown

## API Endpoints

### GET /
Returns the main web interface

### POST /predict
Accepts tumor feature values and returns prediction

**Request:** Form data with feature values  
**Response:** JSON with diagnosis, confidence, and probabilities

### GET /api/info
Returns information about the model

**Response:**
```json
{
  "student_name": "Onipede Toluwani",
  "matric_number": "22CG031936",
  "algorithm": "Logistic Regression",
  "persistence_method": "Joblib",
  "features": ["mean radius", "mean texture", "mean perimeter", "mean area", "mean concavity"],
  "model_loaded": true
}
```

## Deployment

This application can be deployed on:
- Render.com
- PythonAnywhere.com
- Streamlit Cloud
- Vercel
- Scorac.com

For deployment, ensure:
1. All files are uploaded to the platform
2. Dependencies are installed from `requirements.txt`
3. The model files exist in the `model/` directory
4. The Flask app is configured to run on the platform's specified port

## Technologies Used

- **Python 3.14**
- **Flask 3.0.0** - Web framework
- **scikit-learn 1.8.0** - Machine learning
- **pandas 2.3.3** - Data manipulation
- **numpy 2.4.1** - Numerical computing
- **joblib 1.5.3** - Model persistence

## License

This project is for educational purposes only.

## Contact

**Onipede Toluwani**  
Matric No: 22CG031936

