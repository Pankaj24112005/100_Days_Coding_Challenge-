import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("🌸 Iris Prediction App")

# User inputs (with proper ranges)
sepal_length = st.number_input("Sepal Length (cm)", min_value=4.0, max_value=8.0, value=5.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.5)
petal_length = st.number_input("Petal Length (cm)", min_value=1.0, max_value=7.0, value=1.4)
petal_width = st.number_input("Petal Width (cm)", min_value=0.1, max_value=2.5, value=0.2)

# Class labels
species = ["Setosa 🌸", "Versicolor 🌼", "Virginica 🌺"]

if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Flower: {species[prediction[0]]}")