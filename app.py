import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("📊 Customer Churn Prediction System")
st.markdown("Predict whether a telecom customer is likely to churn.")
st.divider()

st.subheader("Customer Profile & Account Information")
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure = st.number_input("Enter Customer Tenure (Months)", min_value=0)

with col2:
    contract = st.selectbox("Select Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment_method = st.selectbox("Payment Method", ["Bank transfer (automatic)", "Credit card (automatic)", "Electronic check", "Mailed check"])
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
    total_charges = st.number_input("Total Charges", min_value=0.0)

st.divider()

st.subheader("Core Services")
col3, col4 = st.columns(2)

with col3:
    phone_service = st.selectbox("Phone Service", ["No", "Yes"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])

with col4:
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

st.divider()

st.subheader("Internet Add-ons & Streaming")
col5, col6, col7 = st.columns(3)

with col5:
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])

with col6:
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])

with col7:
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

st.divider()

if st.button("🔍 Predict Churn"):
    with st.spinner("Analyzing customer data..."):
        
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
            multiple_lines_no_phone = 0
        multiple_lines_yes = 0

        if multiple_lines == "Yes":
            multiple_lines_yes = 1
        elif multiple_lines == "No phone service":
            multiple_lines_no_phone = 1

        online_security_no_internet = 0
        online_security_yes = 0

        if online_security == "Yes":
            online_security_yes = 1
        elif online_security == "No internet service":
            online_security_no_internet = 1

        online_backup_no_internet = 0
        online_backup_yes = 0

        if online_backup == "Yes":
            online_backup_yes = 1
        elif online_backup == "No internet service":
            online_backup_no_internet = 1

        device_protection_no_internet = 0
        device_protection_yes = 0

        if device_protection == "Yes":
            device_protection_yes = 1
        elif device_protection == "No internet service":
            device_protection_no_internet = 1

        streaming_tv_no_internet = 0
        streaming_tv_yes = 0

        if streaming_tv == "Yes":
            streaming_tv_yes = 1
        elif streaming_tv == "No internet service":
            streaming_tv_no_internet = 1

        tech_support_no_internet = 0
        tech_support_yes = 0

        if tech_support == "Yes":
            tech_support_yes = 1
        elif tech_support == "No internet service":
            tech_support_no_internet = 1
        
        multiple_lines_no_phone = 0
        multiple_lines_yes = 0

        if multiple_lines == "Yes" :
            multiple_lines_yes = 1
        elif multiple_lines == "No phone service":
            multiple_lines_no_phone = 1

        streaming_movies_no_internet = 0
        streaming_movies_yes = 0

        if streaming_movies == "Yes":
            streaming_movies_yes = 1
        elif streaming_movies == "No internet service":
            streaming_movies_no_internet = 1

        payment_credit = 0
        payment_electronic = 0
        payment_mailed = 0

        if payment_method == "Credit card (automatic)":
            payment_credit = 1
        elif payment_method == "Electronic check":
            payment_electronic = 1
        elif payment_method == "Mailed check":
            payment_mailed = 1
        
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

        input_df.at[0, 'MultipleLines_No phone service'] = multiple_lines_no_phone
        input_df.at[0, 'MultipleLines_Yes'] = multiple_lines_yes

        input_df.at[0, 'OnlineSecurity_No internet service'] = online_security_no_internet
        input_df.at[0, 'OnlineSecurity_Yes'] = online_security_yes
        
        input_df.at[0, 'OnlineBackup_No internet service'] = online_backup_no_internet
        input_df.at[0, 'OnlineBackup_Yes'] = online_backup_yes

        input_df.at[0, 'DeviceProtection_No internet service'] = device_protection_no_internet
        input_df.at[0, 'DeviceProtection_Yes'] = device_protection_yes

        input_df.at[0, 'TechSupport_No internet service'] = tech_support_no_internet
        input_df.at[0, 'TechSupport_Yes'] = tech_support_yes

        input_df.at[0, 'MultipleLines_No phone service'] = multiple_lines_no_phone
        input_df.at[0, 'MultipleLines_Yes'] = multiple_lines_yes

        input_df.at[0, 'StreamingTV_No internet service'] = streaming_tv_no_internet
        input_df.at[0, 'StreamingTV_Yes'] = streaming_tv_yes

        input_df.at[0, 'StreamingMovies_No internet service'] = streaming_movies_no_internet
        input_df.at[0, 'StreamingMovies_Yes'] = streaming_movies_yes

        input_df.at[0, 'PaymentMethod_Credit card (automatic)'] = payment_credit
        input_df.at[0, 'PaymentMethod_Electronic check'] = payment_electronic
        input_df.at[0, 'PaymentMethod_Mailed check'] = payment_mailed

        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)
        probability = model.predict_proba(input_scaled)
        
        churn_prob = probability[0][1]

        if prediction[0] == 1:
            st.error("⚠️ The customer is likely to churn.")
        else:
            st.success("✅ The customer is not likely to churn.")

        st.subheader("Prediction Confidence")
        st.progress(int(churn_prob * 100))
        
        st.metric(
            label="Churn Probability",
            value=f"{churn_prob * 100:.2f}%"
        )

        if churn_prob >= 0.8:
            st.warning("🚨 Very High Risk Customer")
        elif churn_prob >= 0.5:
            st.info("⚠️ Moderate Risk Customer")
        else:
            st.success("🟢 Low Risk Customer")

        with st.expander("View Encoded Input"):
            st.write(input_df)

st.divider()
st.caption("Built by Jerin Joy using Python, Scikit-learn and Streamlit.")