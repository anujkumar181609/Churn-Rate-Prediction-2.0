# 📊 Telco Customer Churn Prediction using Machine Learning

## 🚀 Project Overview

Customer churn is one of the most critical business problems faced by telecom and subscription-based companies. This project uses Machine Learning techniques to predict whether a customer is likely to leave the company based on their demographic information, subscription details, and service usage patterns.

The goal is to help businesses identify at-risk customers and take proactive retention measures.

---
## 🌐 Live Demo

👉 [Telco Customer Churn Prediction System](https://telco-customer-churn-prediction-te2h2lkha4etbkuve3fwv2.streamlit.app/)]

---
## 🎯 Objectives

* Predict customer churn using machine learning models.
* Compare the performance of multiple classification algorithms.
* Analyze important customer factors affecting churn.
* Deploy a user-friendly prediction interface using Streamlit.
* Assist businesses in improving customer retention strategies.

---

## 📂 Dataset Features

The model uses customer-related information such as:

* Gender
* Senior Citizen Status
* Partner
* Dependents
* Tenure
* Phone Service
* Internet Service
* Online Security
* Device Protection
* Tech Support
* Contract Type
* Payment Method
* Monthly Charges
* Total Charges
* Multiple Lines
* Streaming Services

Target Variable:

```text
Churn
0 → Customer Stays
1 → Customer Leaves
```

---

## 🛠️ Technologies Used

| Category             | Technology            |
| -------------------- | --------------------- |
| Programming Language | Python                |
| Data Analysis        | Pandas, NumPy         |
| Visualization        | Matplotlib, Seaborn   |
| Machine Learning     | Scikit-Learn, XGBoost |
| Model Serialization  | Joblib                |
| Deployment           | Streamlit             |
| Version Control      | Git & GitHub          |

---

## 🔄 Machine Learning Pipeline

### 1️⃣ Data Preprocessing

* Missing value handling
* Feature encoding
* Data cleaning
* Train-Test Split
* Feature scaling

### 2️⃣ Model Training

The following models were trained and evaluated:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Decision Tree
* Random Forest
* XGBoost

### 3️⃣ Model Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix

---

# 📈 Model Performance Comparison

| Model               | Accuracy      | ROC-AUC Score |
| ------------------- | ------------- | ------------- |
| Logistic Regression | **81.08%** 🏆 | **0.7253**    |
| Random Forest       | 80.89%        | 0.7078        |
| SVM                 | 80.42%        | 0.6933        |
| XGBoost             | 80.32%        | 0.7119        |
| Decision Tree       | 78.90%        | 0.6980        |
| KNN                 | 76.82%        | 0.6916        |

---

# 🏆 Best Performing Model

### Logistic Regression

Accuracy:

```text
81.08%
```

ROC-AUC Score:

```text
0.7253
```

Confusion Matrix:

```text
[[699  59]
 [141 158]]
```

Classification Report:

```text
Precision (Churn): 0.73
Recall (Churn):    0.53
F1-Score:          0.61
```

### Why Logistic Regression Won?

* Highest Accuracy
* Highest ROC-AUC Score
* Better Generalization
* Lower Risk of Overfitting
* Strong Baseline Performance

---


# 💻 Streamlit Web Application

The project includes a Streamlit-based web application where users can:

✅ Enter customer information

✅ Predict churn probability

✅ View prediction results instantly

✅ Understand customer retention risks

Run locally:

```bash
streamlit run app.py
```

---

# 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── data/
│   └── customer_churn.csv
│
├── models/
│   └── logistic_regression.pkl
│
├── notebooks/
│   └── churn_prediction.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

---

# 🔮 Future Improvements

* Hyperparameter Optimization
* Feature Importance Dashboard
* SHAP Explainability
* Ensemble Models
* Real-Time API Deployment
* Customer Retention Recommendation Engine

---

# 📚 Key Learnings

Through this project, I gained hands-on experience in:

* Data Cleaning & Preprocessing
* Feature Engineering
* Classification Algorithms
* Model Evaluation
* Streamlit Deployment
* End-to-End Machine Learning Workflow
* Business-Oriented Predictive Analytics

---

# 👨‍💻 Author

**Anuj**

Artificial Intelligence & Machine Learning Student

Passionate about Machine Learning, Data Science, and Building Real-World AI Solutions.

---

⭐ If you found this project useful, consider giving it a star on GitHub!
