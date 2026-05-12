import streamlit as st
import numpy as np
import pickle

# ---------------- LOAD MODEL ---------------- #
model = pickle.load(open("heart_model.pkl", "rb"))

# ---------------- UI ---------------- #
st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️")

st.title("❤️ Heart Disease Prediction App")
st.write("Fill patient details below to predict heart disease risk")

st.subheader("Enter Patient Details")

# ---------------- INPUTS ---------------- #

# AGE
age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    step=1,
    help="Enter age in years (e.g., 45)"
)

# SEX
sex = st.selectbox(
    "Sex",
    ["Male", "Female"],
    help="Male = 1, Female = 0"
)
sex = 1 if sex == "Male" else 0

# CHEST PAIN TYPE
cp_options = {
    0: "Typical Angina",
    1: "Atypical Angina",
    2: "Non-anginal Pain",
    3: "Asymptomatic"
}
cp = st.selectbox(
    "Chest Pain Type",
    list(cp_options.values()),
    help="Type of chest pain"
)
cp = list(cp_options.values()).index(cp)

# RESTING BP
trestbps = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=200,
    help="e.g., 120"
)

# CHOLESTEROL
chol = st.number_input(
    "Cholesterol (mg/dl)",
    min_value=100,
    max_value=600,
    help="e.g., 250"
)

# FASTING BLOOD SUGAR
fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    ["No", "Yes"],
    help="Yes = 1, No = 0"
)
fbs = 1 if fbs == "Yes" else 0

# REST ECG
restecg_options = {
    0: "Normal",
    1: "ST-T abnormality",
    2: "Left ventricular hypertrophy"
}
restecg = st.selectbox(
    "Resting ECG",
    list(restecg_options.values()),
    help="Electrocardiographic result"
)
restecg = list(restecg_options.values()).index(restecg)

# MAX HEART RATE
thalach = st.number_input(
    "Maximum Heart Rate Achieved",
    min_value=60,
    max_value=220,
    help="e.g., 150"
)

# EXERCISE ANGINA
exang = st.selectbox(
    "Exercise Induced Angina",
    ["No", "Yes"],
    help="Yes = 1, No = 0"
)
exang = 1 if exang == "Yes" else 0

scaler = pickle.load(open("scaler.pkl", "rb"))
# OLDPEAK
oldpeak = st.number_input(
    "Oldpeak (ST depression)",
    min_value=0.0,
    max_value=10.0,
    step=0.1,
    help="Decimal allowed (e.g., 1.5)"
)

# SLOPE
slope_options = {
    0: "Upsloping",
    1: "Flat",
    2: "Downsloping"
}
slope = st.selectbox(
    "Slope of ST segment",
    list(slope_options.values()),
    help="Slope type"
)
slope = list(slope_options.values()).index(slope)

# CA
ca = st.selectbox(
    "Number of Major Vessels",
    [0, 1, 2, 3],
    help="e.g., 0 to 3"
)

# THAL
thal_options = {
    1: "Normal",
    2: "Fixed Defect",
    3: "Reversible Defect"
}
thal = st.selectbox(
    "Thalassemia",
    list(thal_options.values()),
    help="Blood disorder type"
)
thal = list(thal_options.values()).index(thal) + 1


# ---------------- PREDICTION ---------------- #

if st.button("Predict"):

    input_data = np.array([[age, sex, cp, trestbps, chol,
                            fbs, restecg, thalach, exang,
                            oldpeak, slope, ca, thal]])

    # Apply scaler (IMPORTANT)
    input_data = scaler.transform(input_data)

    # Prediction only
    prediction = model.predict(input_data)

    st.subheader("Result")

    if prediction[0] == 1:
        st.error("⚠️ Person HAS Heart Disease")
    else:
        st.success("✅ Person does NOT have Heart Disease")

    st.write("Note: This is a prediction, not a medical diagnosis.")