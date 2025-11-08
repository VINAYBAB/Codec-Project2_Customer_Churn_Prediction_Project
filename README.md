# Customer Churn Prediction Project

## Overview
This project predicts customer churn in a telecom setting using classification models. It includes EDA to uncover patterns (e.g., churn by contract type), preprocessing, and model evaluation.

## Features
- Synthetic telecom data generation.
- EDA with visualizations (distributions, correlations).
- Models: Logistic Regression, Random Forest, XGBoost.
- Evaluation: Accuracy, Recall, ROC-AUC, classification reports.
- Feature importance analysis.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Generate data: `python data_generator.py`
3. Run the notebook: `jupyter notebook customer_churn_prediction.ipynb`

## Results
- XGBoost often performs best on imbalanced data.
- EDA reveals patterns like higher churn for month-to-month contracts.

## Extensions
- Handle class imbalance with SMOTE.
- Use real data (e.g., from Kaggle).
- Deploy as a web app with Streamlit.
