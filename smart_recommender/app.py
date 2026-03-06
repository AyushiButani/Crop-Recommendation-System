import streamlit as st
import joblib
import numpy as np

# 1. Load the "Saved Brain" (The model we dumped in the notebook)
model = joblib.load('crop_model.pkl')

st.title("🌿 Smart Crop Recommender")
st.write("Enter soil details below to get a prediction.")

# 2. Create the input boxes for the user
n = st.number_input("Nitrogen", 0, 150)
p = st.number_input("Phosphorus", 0, 150)
k = st.number_input("Potassium", 0, 210)
temp = st.number_input("Temperature (°C)", 0.0, 50.0)
hum = st.number_input("Humidity (%)", 0.0, 100.0)
ph = st.number_input("pH level", 0.0, 14.0)
rain = st.number_input("Rainfall (mm)", 0.0, 500.0)

# 3. The "Predict" Button logic
if st.button("Predict Best Crop"):
    # Organize the inputs into the format the model expects
    input_data = np.array([[n, p, k, temp, hum, ph, rain]])
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    # Show the result in a nice green box
    st.success(f"Recommended Crop: {prediction[0].upper()}")
    