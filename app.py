
import streamlit as st
import pickle
import numpy as np

# Load trained model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ------------------- Setup Logging -------------------
logging.basicConfig(
    filename="loan_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

st.title("Loan Eligibility Prediction App")

# Input fields
income = st.number_input("Applicant's Monthly Income", min_value=0)
coincome = st.number_input("Co-Applicant's Monthly Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.selectbox("Loan Term (in months)", [12, 36, 60, 84, 120, 180, 240, 300, 360, 480])
credit_history = st.selectbox("Credit History", [1, 0])

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

if st.button("Submit"):
    # One-hot encode the inputs
    gender_female = 1 if gender == "Female" else 0
    gender_male = 1 if gender == "Male" else 0
    married_no = 1 if married == "No" else 0
    married_yes = 1 if married == "Yes" else 0
    dep_0 = 1 if dependents == "0" else 0
    dep_1 = 1 if dependents == "1" else 0
    dep_2 = 1 if dependents == "2" else 0
    dep_3p = 1 if dependents == "3+" else 0
    edu_grad = 1 if education == "Graduate" else 0
    edu_not = 1 if education == "Not Graduate" else 0
    self_no = 1 if self_employed == "No" else 0
    self_yes = 1 if self_employed == "Yes" else 0
    area_rural = 1 if property_area == "Rural" else 0
    area_semi = 1 if property_area == "Semiurban" else 0
    area_urban = 1 if property_area == "Urban" else 0

    features = [[
        income, coincome, loan_amount, loan_term, credit_history,
        gender_female, gender_male, married_no, married_yes,
        dep_0, dep_1, dep_2, dep_3p,
        edu_grad, edu_not, self_no, self_yes,
        area_rural, area_semi, area_urban
    ]]

    # Scale features
    scaled_features = scaler.transform(features)

    prediction = model.predict(scaled_features)
    if prediction[0] == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Not Approved.")
