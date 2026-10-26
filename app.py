
import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("models/churn_model.pkl")

# App Title
st.title("Churn Prediction App")
st.write("This App Predict Whether a Customer will Churn or Not")

# Customer Inputs
age = st.number_input(
    "Enter Customer Age",
    min_value=18,
    max_value=100,
    value=30,
    step=1
)

tenure_months = st.number_input(
    "Enter Customer Tenure",
    min_value=0,
    max_value=100,
    value=12,
    step=1
)

contract_type = st.selectbox(
    "Contract Type",
    options=["Month-to-Month", "Two-year", "Yearly"]
)

monthly_charges = st.number_input(
    "Enter Monthly Charges",
    min_value=0.0,
    max_value=1000.0,
    value=500.0,
    step=0.1
)

support_calls = st.number_input(
    "Enter Number of Support Calls",
    min_value=0,
    max_value=100,
    value=2,
    step=1
)

data_usage_gb = st.number_input(
    "Enter Data Usage in GB",
    min_value=0.0,
    max_value=1000.0,
    value=10.0,
    step=0.1
)

total_charges = st.number_input(
    "Enter Total Charges",
    min_value=0.0,
    max_value=10000.0,
    value=5000.0,
    step=0.1
)

payment_method = st.selectbox(
    "Payment Method",
    options=["Cash", "NetBanking", "UPI"]
)

# Center Predict Button
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    predict_button = st.button(
        "Predict",
        use_container_width=True
    )

# Prediction
if predict_button:

    input_data = pd.DataFrame({
        "age": [age],
        "tenure_months": [tenure_months],
        "monthly_charges": [monthly_charges],
        "support_calls": [support_calls],
        "data_usage_gb": [data_usage_gb],
        "total_charges": [total_charges],
        "contract_type": [contract_type],
        "payment_method": [payment_method]
    })

    # Encode Categorical Columns
    input_data = pd.get_dummies(
        input_data,
        columns=["contract_type", "payment_method"],
        drop_first=True,
        dtype=int
    )

    # Match Training Columns
    input_data = input_data.reindex(
        columns=model.get_booster().feature_names,
        fill_value=0
    )

    # Make Prediction
    prediction = model.predict(input_data)

    # Display Result
    if prediction[0] == 1:
        st.error("Customer is likely to CHURN!")
    else:
        st.success("Customer is NOT likely to CHURN!")

