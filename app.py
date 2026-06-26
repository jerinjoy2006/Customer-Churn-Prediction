import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("Customer Churn Prediction")

tenure = st.number_input(
    "Enter Customer Tenure (Months)",
    min_value=0
)

contract = st.selectbox(
    "Select Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

senior = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.selectbox(
    "Partner",
    ["No", "Yes"]
)

dependents = st.selectbox(
    "Dependents",
    ["No", "Yes"]
)

phone_service = st.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

if st.button("Predict"):

    gender_value = 1 if gender == "Male" else 0
    partner_value = 1 if partner == "Yes" else 0
    dependents_value = 1 if dependents == "Yes" else 0
    phone_service_value = 1 if phone_service == "Yes" else 0
    paperless_billing_value = 1 if paperless_billing == "Yes" else 0

    contract_one_year = 0
    contract_two_year = 0

    if contract == "One year":
        contract_one_year = 1
    elif contract == "Two year":
        contract_two_year = 1

    internet_fiber = 0
    internet_no = 0

    if internet_service == "Fiber optic":
        internet_fiber = 1
    elif internet_service == "No":
        internet_no = 1

    input_df = pd.DataFrame(columns=model_columns)
    input_df.loc[0] = 0

    input_df.at[0, 'gender'] = gender_value
    input_df.at[0, 'SeniorCitizen'] = senior
    input_df.at[0, 'Partner'] = partner_value
    input_df.at[0, 'Dependents'] = dependents_value
    input_df.at[0, 'tenure'] = tenure

    input_df.at[0, 'PhoneService'] = phone_service_value
    input_df.at[0, 'PaperlessBilling'] = paperless_billing_value
    input_df.at[0, 'MonthlyCharges'] = monthly_charges
    input_df.at[0, 'TotalCharges'] = total_charges

    input_df.at[0, 'Contract_One year'] = contract_one_year
    input_df.at[0, 'Contract_Two year'] = contract_two_year

    input_df.at[0, 'InternetService_Fiber optic'] = internet_fiber
    input_df.at[0, 'InternetService_No'] = internet_no

    st.write(input_df)
    
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    if prediction[0] == 1:
        st.error("The customer is likely to churn.")
    else:
        st.success("The customer is not likely to churn.")

    probability = model.predict_proba(input_scaled)
    st.write("Churn Probability:", round(probability[0][1] * 100, 2), "%")