import numpy as np
from sklearn.linear_model import LogisticRegression

# Features: [Usage Minutes, Contract Duration (months)]
X = np.array([
    [200, 1], [150, 2], [450, 12], [500, 24],
    [100, 1], [600, 12], [120, 3], [700, 24]
])
# Churn: 1 = Churned, 0 = Retained
y = np.array([1, 1, 0, 0, 1, 0, 1, 0])

model = LogisticRegression()
model.fit(X, y)

new_customer = np.array([[180, 2]])
churn_pred = model.predict(new_customer)[0]
prob = model.predict_proba(new_customer)[0]

print("Customer Churn Prediction (Logistic Regression):")
print(f"Customer Input: Usage=180 mins, Contract=2 months")
print(f"Churn Prediction: {'Churn (1)' if churn_pred == 1 else 'Retained (0)'}")
print(f"Churn Probability: {prob[1]*100:.2f}%")
