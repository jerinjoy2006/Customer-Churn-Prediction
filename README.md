# 📊 Customer Churn Prediction System

A Machine Learning web application that predicts whether a telecom customer is likely to churn (leave the company) based on customer demographics, account information, and subscribed services.

## 🌐 Live Demo

🔗 https://customer-churn-prediction2134.streamlit.app/

---

## 📖 Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. Acquiring a new customer is significantly more expensive than retaining an existing one. This project uses Machine Learning to identify customers who are likely to churn so that businesses can take proactive measures to retain them.

The application allows users to enter customer information through an interactive web interface and instantly receive:

* Churn Prediction (Likely to Churn / Not Likely to Churn)
* Churn Probability
* Customer Risk Category

---

## 🎯 Objectives

* Analyze customer churn patterns.
* Build and evaluate Machine Learning models.
* Deploy the model using Streamlit.
* Create an interactive and user-friendly prediction system.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

### Tools

* Jupyter Notebook
* VS Code
* Git & GitHub
* Streamlit Community Cloud

---

## 📂 Dataset

Dataset: Telco Customer Churn Dataset

Features include:

* Gender
* Senior Citizen Status
* Partner
* Dependents
* Tenure
* Contract Type
* Internet Service
* Payment Method
* Monthly Charges
* Total Charges
* Additional Services

Target Variable:

* Churn

  * 1 → Customer will churn
  * 0 → Customer will not churn

---

## 📊 Exploratory Data Analysis (EDA)

Performed:

* Missing value analysis
* Data cleaning and preprocessing
* Correlation analysis
* Distribution plots
* Churn analysis by:

  * Contract Type
  * Internet Service
  * Tenure
  * Monthly Charges
  * Payment Method

---

## ⚙️ Data Preprocessing

* Handled missing values.
* Converted categorical variables into numerical variables using One-Hot Encoding.
* Scaled numerical features using StandardScaler.
* Split the dataset into:

  * Training Set: 80%
  * Testing Set: 20%

---

## 🤖 Machine Learning Models

### Logistic Regression

* Accuracy: 82.04%
* Used StandardScaler.
* Interpretable through feature coefficients.

### Random Forest Classifier

* Accuracy: ~79.56%
* Used for comparison.

### Final Selected Model

✅ Logistic Regression

Reason:

* Better performance.
* Better interpretability.
* Simpler deployment.

---

## 📈 Model Performance

### Logistic Regression Results

Accuracy: **82.04%**

Classification Report:

* Precision (Churn): 0.69
* Recall (Churn): 0.60
* F1-Score (Churn): 0.64

Confusion Matrix:

| Actual / Predicted | No Churn | Churn |
| ------------------ | -------- | ----- |
| No Churn           | 934      | 102   |
| Churn              | 151      | 222   |

---

## 🚀 Web Application Features

* Interactive user interface.
* Real-time churn prediction.
* Churn probability score.
* Customer risk categorization.
* Input validation.
* Deployed online using Streamlit.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/jerinjoy2006/Customer-Churn-Prediction.git
```

Navigate to the project folder:

```bash
cd your-repository-name
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── customer_churn.ipynb
├── churn_model.pkl
├── scaler.pkl
├── model_columns.pkl
├── requirements.txt
├── README.md
└── images/
```

---

## 🔮 Future Improvements

* Hyperparameter tuning.
* Additional ML models such as XGBoost.
* SHAP explanations for predictions.
* Customer retention recommendations.
* Database integration.
* User authentication system.

---

## 📚 Key Learnings

Through this project, I gained practical experience in:

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Machine Learning Model Building
* Model Evaluation
* Model Deployment
* Git and GitHub
* Building Interactive Web Applications with Streamlit

---

## 👨‍💻 Author

**Jerin Joy**

* GitHub: https://github.com/jerinjoy2006
* Live App: https://customer-churn-prediction2134.streamlit.app/

---

⭐ If you found this project useful, please consider giving it a star.
