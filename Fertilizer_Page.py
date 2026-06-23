import streamlit as st
import numpy as np
import pickle


def app():
    # Load trained model
    model, soil_encoder, crop_encoder, fert_encoder = pickle.load(
        open("fertilizer_model.pkl", "rb")
    )

    #st.set_page_config(page_title="Fertilizer Recommendation", layout="centered")

    st.title("🌱 Fertilizer Recommendation System")
    st.write("Provide soil and crop details to get the best fertilizer suggestion.")

    # ---------------- INPUT FIELDS ---------------- #

    temperature = st.number_input("🌡 Temperature (°C)", min_value=0.0)
    humidity = st.number_input("💧 Humidity (%)", min_value=0.0)
    moisture = st.number_input("🌾 Soil Moisture (%)", min_value=0.0)

    soil_type = st.selectbox("🪨 Soil Type",
                             ["Sandy", "Loamy", "Black", "Red", "Clayey"])

    crop_type = st.selectbox("🌿 Crop Type",
                             ["Rice", "Wheat", "Maize", "Sugarcane", "Cotton", "Tobacco", "Barley", "Millets", "Oil seeds",
                              "Pulses"])

    nitrogen = st.number_input("🧪 Nitrogen (N)", min_value=0)
    phosphorus = st.number_input("🧪 Phosphorus (P)", min_value=0)
    potassium = st.number_input("🧪 Potassium (K)", min_value=0)

    # ---------------- ENCODING ---------------- #

    soil_dict = {
        "Sandy": 0,
        "Loamy": 1,
        "Black": 2,
        "Red": 3,
        "Clayey": 4
    }

    crop_dict = {
        "Rice": 0,
        "Wheat": 1,
        "Maize": 2,
        "Sugarcane": 3,
        "Cotton": 4,
        "Tobacco": 5,
        "Barley": 6,
        "Millets": 7,
        "Oil seeds": 8,
        "Pulses": 9
    }

    # ---------------- PREDICTION ---------------- #

    if st.button("🌟 Recommend Fertilizer"):

        soil_encoded = soil_encoder.transform([soil_type])[0]
        crop_encoded = crop_encoder.transform([crop_type])[0]

        input_data = np.array([[
            temperature,
            humidity,
            moisture,
            soil_encoded,
            crop_encoded,
            nitrogen,
            phosphorus,
            potassium
        ]])

        prediction = model.predict(input_data)
        fertilizer_name = fert_encoder.inverse_transform(prediction)

        st.success(f"✅ Recommended Fertilizer: {fertilizer_name[0]}")