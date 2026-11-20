import numpy as np
from sklearn.linear_model import LinearRegression

# Features: [Area (sqft), Bedrooms, Bathrooms]
X = np.array([
    [1200, 2, 1], [1500, 3, 2], [1800, 3, 2], [2200, 4, 3],
    [2500, 4, 3], [3000, 5, 4], [3500, 5, 4]
])
# Price ($)
y = np.array([250000, 320000, 370000, 450000, 520000, 630000, 720000])

model = LinearRegression()
model.fit(X, y)

new_house = np.array([[2000, 3, 2]])
pred_price = model.predict(new_house)[0]

print("Housing Price Linear Regression Model:")
print(f"Features: Area=2000 sqft, Bedrooms=3, Bathrooms=2")
print(f"Predicted House Price: ${pred_price:,.2f}")
print(f"Model R² Score: {model.score(X, y):.4f}")
