# 🩺 Diabetes Prediction ML Microservice

This project is a Machine Learning microservice built using **Django REST Framework**.  
It predicts whether a person is diabetic or not based on user input parameters such as glucose level, BMI, insulin, and age.  
The API exposes a `/predict` endpoint that accepts JSON input and returns the prediction along with a confidence score.

---

## 🚀 Features
- End-to-end Machine Learning model integration
- REST API endpoint: `/predict`
- Accepts JSON input, returns JSON output
- Dockerized for easy deployment
- Supports real-time prediction via web or API
- Includes model confidence score in the output

---

## 🧠 Tech Stack
- **Python 3.10**
- **Django** & **Django REST Framework**
- **Scikit-learn**, **NumPy**, **Joblib**
- **Docker**

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/diabetes-prediction-api.git
cd diabetes-prediction-api
