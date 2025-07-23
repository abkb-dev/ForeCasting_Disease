import streamlit as st

# Set page title and description
st.set_page_config(page_title="Prognosis Pulse WebApp", page_icon="🌡️")
st.image("home.jpeg")
st.title("Welcome to Prognosis Pulse WebApp")
st.write("This Web Application is designed to help users predict the likelihood of developing certain diseases based on their input features. With the use of trained and tested machine learning models, we provide predictions for Diabetes, Heart Disease, Lung Cancer, and more.")

# Project Overview
#st.header("Project Overview")
#st.write("Prognosis Pulse integrates various health-related features to assist users in making informed decisions. Here are some key components:")

# Chatbots
st.subheader("Chatbots:")
st.write("We have two chatbots:")
st.markdown("- **DietNutribot**: Provides personalized dietary recommendations based on user profiles and health conditions.")
st.markdown("- **FitGuide360Bot**: Offers fitness guidance, exercise routines, and wellness tips.")

# EHR Integration
st.subheader("EHR Integration:")
st.write("Our platform seamlessly integrates Electronic Health Records (EHR) to ensure accurate data input and personalized predictions.")

# Community Engagement
st.subheader("Community Engagement:")
st.write("Connect with other users, share experiences, and participate in health-related discussions through our community engagement platform.")

# Telemedicine Services
st.subheader("Telemedicine Services:")
st.write("Access virtual consultations with healthcare professionals, schedule appointments, and receive expert advice.")

# How to Use
st.header("How to Use:")
st.write("1. Navigate to the Main Menu (>) located in the top-left corner of the screen.")
st.write("2. Click on the desired tab among 'Diabetes Prediction', 'Heart Disease', and 'Lung Cancer' to access prediction tools for specific diseases.")
st.write("3. Enter relevant information as requested in the input fields.")
st.write("4. Click on the 'Test Result' button to obtain predictions based on the provided data.")

# Disclaimer
st.header("Disclaimer:")
st.write("This Web App may not provide accurate predictions at all times. When in doubt, please enter the values again and verify the predictions.")
st.write("You are requested to provide your Name and Email for sending details about your test results. Rest assured, your information is safe and will be kept confidential.")
st.write("It is important to note that individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.")
