import streamlit as st
import pandas as pd

st.title("BMI Calculator")

# Fixing syntax errors in sliders
height = st.slider("Select your Height (in cm):", 100, 250, 175)
weight = st.slider("Select your Weight (in kg):", 40, 270, 101)

# Correcting BMI calculation
bmi = weight / ((height / 100) ** 2)

# Display BMI
st.write(f"Your BMI is {bmi:.2f}")

# Display BMI categories
st.write("### BMI Category ###")
st.write("- **Underweight:** BMI less than 18.5")
st.write("- **Normal weight:** BMI between 18.5 and 24.9")
st.write("- **Overweight:** BMI between 25 and 29.9")
st.write("- **Obesity:** BMI 30 or greater")
