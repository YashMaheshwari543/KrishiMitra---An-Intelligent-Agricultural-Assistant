import streamlit as st
import numpy as np
import pickle

def app():
    # Load model properly
    loaded_data = pickle.load(open("model.pkl", "rb"))

    # Handle different cases
    if isinstance(loaded_data, list):
        model = loaded_data[0]  # extract model
    else:
        model = loaded_data

    st.title("🌾 Crop Recommendation System")

    st.write("Enter soil and weather details:")

    # Inputs
    N = st.number_input("Nitrogen")
    P = st.number_input("Phosphorus")
    K = st.number_input("Potassium")
    temperature = st.number_input("Temperature")
    humidity = st.number_input("Humidity")
    ph = st.number_input("pH")
    rainfall = st.number_input("Rainfall")

    # Prediction
    if st.button("Predict Crop"):
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

        prediction = model.predict(input_data)

        st.success(f"Recommended Crop: {prediction[0]}")