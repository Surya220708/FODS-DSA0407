import numpy as np
from sklearn.tree import DecisionTreeRegressor

# Features: [Mileage (k miles), Age (years), Engine Size (L)]
X = np.array([
    [20, 2, 2.0], [45, 4, 1.8], [70, 6, 2.5], [100, 8, 1.6],
    [30, 3, 2.4], [15, 1, 3.0], [85, 7, 2.0], [120, 10, 1.5]
])
# Price ($)
y = np.array([28000, 20000, 16000, 11000, 24000, 34000, 13000, 8500])

cart = DecisionTreeRegressor(max_depth=3, random_state=42)
cart.fit(X, y)

new_car = np.array([[35, 3, 2.0]])
pred_price = cart.predict(new_car)[0]
decision_path = cart.decision_path(new_car)

print("CART Car Price Prediction & Decision Path:")
print(f"Input Car: Mileage=35k miles, Age=3 years, Engine=2.0L")
print(f"Predicted Car Price: ${pred_price:,.2f}")
print(f"Decision Path Nodes Visited: {decision_path.indices.tolist()}")
