
# 🏦 Loan Eligibility Prediction App

A real-time, interactive web application built with **Streamlit** that predicts whether a loan applicant is eligible for a loan based on financial and demographic data. The project uses a trained **Logistic Regression** model, modular Python code, and a clean UI to assist users in quick and explainable decision-making.

---

## 🚀 Features

- ✅ Predict loan eligibility based on 10 input parameters
- ✅ Real-time, user-friendly web interface via Streamlit
- ✅ Modular code structure for maintainability
- ✅ Model and scaler stored with `pickle` for deployment
- ✅ Well-structured project and clean folder hierarchy
- ✅ Proper logging, error handling, and readable code

---

## 📁 Project Structure

```
loan_eligibility_modular/
├── app.py                  # Streamlit web app
├── requirements.txt        # Python dependencies
├── models/
│   ├── model.pkl           # Trained Logistic Regression model
│   └── scaler.pkl          # StandardScaler for input data
├── data/
│   └── credit.csv          # Loan applicant dataset
└── src/
    ├── data_loader.py      # Loads and preprocesses data
    ├── model.py            # Loads trained model and scaler
    └── predictor.py        # Generates predictions
```

---

## ⚙️ How to Run the App

### 🔁 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Loan_Eligibility_Prediction.git
cd Loan_Eligibility_Prediction
```

### 📦 Step 2: Install Dependencies

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

### ▶️ Step 3: Run the App

```bash
streamlit run app.py
```

> The app will launch in your default browser on `http://localhost:8501`

---

## 🧠 Model Info

- **Algorithm**: Logistic Regression
- **Scaler**: StandardScaler
- **Input Features**:
  - Applicant Income
  - Co-applicant Income
  - Loan Amount
  - Loan Term
  - Credit History
  - Gender
  - Marital Status
  - Education
  - Self Employment
  - Property Area
- **Output**: Eligible (`1`) or Not Eligible (`0`)

---

## 📊 Dataset

- `credit.csv`: contains anonymized applicant data
- Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/) (or your custom data)

---

## 🎯 Future Enhancements

- 🌐 Deploy on Streamlit Community Cloud / Heroku
- 📈 Improve model performance with Random Forest or XGBoost
- 🧾 Add explanations (SHAP/LIME) to improve transparency
- 📊 Connect to real-time data APIs
- 🔐 Add user authentication for multi-user access

---

## 📧 Contact

**Author**: Nikhil Teotia  
📍 Ottawa, Canada  
✉️ teot0001@algonquinlive.com  
🔗 [LinkedIn](https://www.linkedin.com/in/nikhil-teotia-a532a21a5)

---

> 📘 This project was completed as part of the CST2216 – Business Intelligence System Infrastructure course at Algonquin College.
