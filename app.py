#importing libraries
import streamlit as st
import pandas as pd
import joblib 
from pathlib import Path

# Page Config
st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# Load Model
BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / "churn_model.pkl"
model= joblib.load(open(model_path, 'rb'))

# Custom CSS
st.markdown("""
<style>
.metric-card{
    background-color:#1E1E1E;
    padding:20px;
    border-radius:15px;
    border:1px solid #333333;
    text-align:center;
}
.metric-value{
    font-size:28px;
    font-weight:bold;
    color:#4CAF50;
}
.metric-title{
    font-size:16px;
    color:#BDBDBD;
}
.pred-box{
    padding:20px;
    border-radius:15px;
    font-size:22px;
    font-weight:bold;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.title("📌 Project Overview")

    st.markdown("""
### Telco Customer Churn Prediction System

This machine learning application predicts whether a customer is likely to churn based on account, billing and service information.

### Selected Features
- Tenure
- Contract Type
- Monthly Charges
- Total Charges
- Internet Service
- Online Security
- Tech Support
- Multiple Lines
- Paperless Billing
- Payment Method

### Model
**Logistic Regression**

Feature Selection + Model Comparison performed before final deployment.

---
""")

    st.success("ROC-AUC Score: 86.16%")
    
    st.markdown("---")

    st.caption("Developed by Anuj Kumar")


# Header
st.title("📊 Telco Customer Churn Prediction")
st.markdown(
    "Predict whether a customer is likely to leave the service."
)


# Input Section
col1, col2 = st.columns(2)

with col1:

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        value=None,
        placeholder="Enter tenure"
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=None,
        placeholder="Enter total charges"
    )

    contract = st.selectbox(
        "Contract Type",
        ["", "Month-to-month", "One year", "Two year"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["", "DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["", "Yes", "No"]
    )

with col2:

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=None,
        placeholder="Enter monthly charges"
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["", "Yes", "No"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["", "Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["", "Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "",
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


# Predict Button
st.markdown("")

if st.button("🔍 Predict Churn", use_container_width=True):

    input_data = pd.DataFrame({
        "tenure":[tenure],
        "Contract":[contract],
        "TotalCharges":[total_charges],
        "InternetService":[internet_service],
        "OnlineSecurity":[online_security],
        "PaperlessBilling":[paperless_billing],
        "TechSupport":[tech_support],
        "MultipleLines":[multiple_lines],
        "PaymentMethod":[payment_method],
        "MonthlyCharges":[monthly_charges]
    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.markdown("---")

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error(
            f"⚠️ Customer likely to Churn\n\nProbability: {probability:.2%}"
        )

    else:

        st.success(
            f"✅ Customer likely to Stay\n\nProbability: {(1-probability):.2%}"
        )

    # Risk Level

    st.subheader("Risk Level")

    if probability < 0.30:
        st.success("🟢 Low Risk")

    elif probability < 0.60:
        st.warning("🟡 Medium Risk")

    else:
        st.error("🔴 High Risk")
d by Anuj Kumar
""")
