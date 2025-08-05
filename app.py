
import streamlit as st
import logging
import os
from src.model import load_model, load_scaler
from src.predictor import make_prediction

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

st.set_page_config(page_title="Loan Eligibility Predictor", layout="centered")
st.title("🏦 Loan Eligibility Prediction App")
st.markdown("---")

try:
    model = load_model("models/model.pkl")
    scaler = load_scaler("models/scaler.pkl")
    logging.info("Model and scaler loaded successfully.")
except Exception as e:
    logging.exception("Failed to load model or scaler.")
    st.error("❌ Error loading model or scaler. Please check logs.")
    st.stop()

# User inputs
income = st.number_input("Applicant's Monthly Income (₹)", min_value=0)
coincome = st.number_input("Co-Applicant's Monthly Income (₹)", min_value=0)
loan_amount = st.number_input("Loan Amount (₹)", min_value=0)
loan_term = st.selectbox("Loan Term (in months)", [12, 36, 60, 84, 120, 180, 240, 300, 360])
credit_history = st.radio("Credit History", [1, 0], format_func=lambda x: "Good (1)" if x == 1 else "Bad (0)")
gender = st.radio("Gender", [1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
married = st.radio("Married", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
education = st.radio("Education", [1, 0], format_func=lambda x: "Graduate" if x == 1 else "Not Graduate")
self_employed = st.radio("Self-Employed", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
property_area = st.selectbox("Property Area", [0, 1, 2], format_func=lambda x: ["Rural", "Semiurban", "Urban"][x])

if st.button("Predict Eligibility"):
    try:
        result = make_prediction(
            model, scaler, income, coincome, loan_amount, loan_term,
            credit_history, gender, married, education, self_employed, property_area
        )
        if result == 1:
            st.success("✅ Eligible for Loan")
            logging.info("Prediction: Eligible")
        else:
            st.error("❌ Not Eligible for Loan")
            logging.info("Prediction: Not Eligible")
    except Exception as e:
        st.error("❌ Prediction failed. Check logs.")
        logging.exception("Error during prediction")
