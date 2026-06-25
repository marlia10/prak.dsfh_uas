import streamlit as st
import joblib

# Membaca model
model = joblib.load("gradient_boosting.pkl")

st.title("Prediksi AIDS Clinical Trial")

st.success("Model Gradient Boosting berhasil dimuat")
