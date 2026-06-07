import streamlit as st
import pandas as pd
import joblib

# Load saved files
model = joblib.load("KNN_Heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

st.set_page_config(page_title="Heart Disease Prediction")

st.title("❤️ Heart Disease Prediction")
st.write("Enter patient details below:")

# Inputs
age = st.slider("Age", 18, 100, 40)

sex = st.selectbox(
    "Sex",
    ["M", "F"]
)

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "TA", "ASY"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=250,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol (mg/dl)",
    min_value=0,
    max_value=700,
    value=200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    [0, 1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.number_input(
    "Maximum Heart Rate Achieved",
    min_value=60,
    max_value=220,
    value=150
)

exercise_angina = st.selectbox(
    "Exercise Induced Angina",
    ["N", "Y"]
)

oldpeak = st.number_input(
    "Oldpeak (ST Depression)",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)

if st.button("Predict"):

    # Create dataframe with all expected columns
    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=expected_columns
    )

    # Numerical features
    input_df.loc[0, "Age"] = age
    input_df.loc[0, "RestingBP"] = resting_bp
    input_df.loc[0, "Cholesterol"] = cholesterol
    input_df.loc[0, "FastingBS"] = fasting_bs
    input_df.loc[0, "MaxHR"] = max_hr
    input_df.loc[0, "Oldpeak"] = oldpeak

    # Sex
    if sex == "M":
        input_df.loc[0, "Sex_M"] = 1

    # Chest Pain Type
    if chest_pain == "ATA":
        input_df.loc[0, "ChestPainType_ATA"] = 1
    elif chest_pain == "NAP":
        input_df.loc[0, "ChestPainType_NAP"] = 1
    elif chest_pain == "TA":
        input_df.loc[0, "ChestPainType_TA"] = 1
    # ASY -> all zeros

    # Resting ECG
    if resting_ecg == "Normal":
        input_df.loc[0, "RestingECG_Normal"] = 1
    elif resting_ecg == "ST":
        input_df.loc[0, "RestingECG_ST"] = 1
    # LVH -> all zeros

    # Exercise Angina
    if exercise_angina == "Y":
        input_df.loc[0, "ExerciseAngina_Y"] = 1
    # N -> 0

    # ST Slope
    if st_slope == "Flat":
        input_df.loc[0, "ST_Slope_Flat"] = 1
    elif st_slope == "Up":
        input_df.loc[0, "ST_Slope_Up"] = 1
    # Down -> 0

    # Scale
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)[0]

    # Probability
    probability = model.predict_proba(input_scaled)[0]
    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
        st.write(f"Confidence: {confidence}%")
    else:
        st.success("✅ Low Risk of Heart Disease")
        st.write(f"Confidence: {confidence}%")