import pandas as pd
import numpy as np
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic data (1000 customers)
n_customers = 1000

# Features
tenure = np.random.randint(1, 73, n_customers)  # Months
monthly_charges = np.random.uniform(20, 120, n_customers)
contract = np.random.choice(['Month-to-month', 'One year', 'Two year'], n_customers, p=[0.55, 0.25, 0.20])
internet_service = np.random.choice(['DSL', 'Fiber optic', 'No'], n_customers, p=[0.35, 0.45, 0.20])
payment_method = np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], n_customers)
gender = np.random.choice(['Male', 'Female'], n_customers)
senior_citizen = np.random.choice([0, 1], n_customers, p=[0.84, 0.16])
dependents = np.random.choice(['Yes', 'No'], n_customers, p=[0.3, 0.7])

# Churn logic: Higher churn for short tenure, high charges, month-to-month contracts
churn_prob = (1 / tenure) * 0.1 + (monthly_charges / 120) * 0.3 + (contract == 'Month-to-month') * 0.4
churn = np.random.binomial(1, churn_prob, n_customers).astype(bool)

# Create DataFrame
df = pd.DataFrame({
    'customerID': [f'CUST{i:04d}' for i in range(n_customers)],
    'gender': gender,
    'SeniorCitizen': senior_citizen,
    'Dependents': dependents,
    'tenure': tenure,
    'MonthlyCharges': monthly_charges,
    'Contract': contract,
    'InternetService': internet_service,
    'PaymentMethod': payment_method,
    'Churn': churn
})

# Save to CSV
df.to_csv('data/churn_data.csv', index=False)
print("Synthetic churn data generated and saved to data/churn_data.csv")
