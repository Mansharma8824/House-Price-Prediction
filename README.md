# 🏠 House Price Prediction System

A Machine Learning web application that predicts Bangalore house prices based on property features such as square feet area, number of bathrooms, BHK, and location.

This project demonstrates the complete Machine Learning workflow including:
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Model Training
- Model Evaluation
- Flask Integration
- Web Application Deployment

The application allows users to enter house details through a simple web interface and instantly get the predicted house price.

---

# 🚀 Features

- Predict house prices using Machine Learning
- User-friendly Flask web application
- Location-based price prediction
- Data preprocessing and feature engineering
- One-Hot Encoding for categorical features
- Multiple ML models implementation
- Model evaluation using R² Score and MAE
- Responsive HTML frontend

---

# 🛠️ Tech Stack

## Machine Learning
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Backend
- Flask

## Frontend
- HTML
- CSS

## Deployment
- Render / Railway / PythonAnywhere

---

# 📂 Project Structure

house-price-prediction/
│
├── app/
│   ├── static/
│   │   └── style.css
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── models/
│   │   └── house_price_model.pkl
│   │
│   └── app.py
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── feature_engineering.ipynb
│   └── model_training.ipynb
│
├── data/
│   └── Bengaluru_House_Data.csv
│
├── screenshots/
│   ├── home.png
│   └── prediction.png
│
├── requirements.txt
├── README.md
└── .gitignore

---

# 📊 Dataset Information

The dataset contains Bangalore housing data with multiple features including:

- Location
- Total Square Feet
- Bathrooms
- Balcony
- BHK
- Price

## Data Preprocessing Steps

- Handling missing values
- Removing outliers
- Feature engineering
- Converting categorical variables
- One-hot encoding
- Scaling and cleaning data

---

# 🤖 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Outlier Detection & Removal
6. Model Training
7. Hyperparameter Tuning
8. Model Evaluation
9. Flask Integration
10. Deployment

---

# 🧠 Models Used

The following Machine Learning models were tested:

- Linear Regression
- Ridge Regression
- Lasso Regression

Final model selection was based on model performance and evaluation metrics.

---

# 📈 Model Performance

## Evaluation Metrics

- R² Score: 0.78
- Mean Absolute Error (MAE): 0.14

The model achieved good prediction accuracy after performing feature engineering and outlier handling.

---

# 🖥️ Application Screenshots

## Home Page

![Home Page](screenshots/home.png)

## Prediction Result

![Prediction Result](screenshots/prediction.png)

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction