# Heart-Disease-Predictor
Developed a Heart Disease Prediction System using K-Nearest Neighbors (KNN) and Streamlit. Implemented data preprocessing, feature scaling, model training, and real-time prediction with an interactive web interface, achieving approximately 87% accuracy.

# ❤️ Heart Disease Prediction System

A Machine Learning web application that predicts the likelihood of heart disease using patient health parameters.

## Features

* Predicts heart disease risk using K-Nearest Neighbors (KNN)
* Interactive Streamlit user interface
* Real-time predictions
* Data preprocessing and feature scaling
* Probability-based confidence score

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* Streamlit
* Joblib

## Dataset Features

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise Induced Angina
* Oldpeak
* ST Slope

## Model

* Algorithm: K-Nearest Neighbors (KNN)
* Feature Scaling: StandardScaler
* Accuracy: ~87%

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

```text
app.py
KNN_Heart.pkl
scaler.pkl
columns.pkl
requirements.txt
README.md
```
