import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# House Size (sqft) vs Price ($1000s)
house_size = np.array([[850], [1100], [1400], [1650], [1900], [2300], [2600], [3100]])
price = np.array([170, 215, 270, 310, 360, 430, 485, 590])

corr = np.corrcoef(house_size.flatten(), price)[0, 1]
model = LinearRegression()
model.fit(house_size, price)
pred = model.predict(house_size)

print("Real Estate Bivariate Regression Analysis:")
print(f"Pearson Correlation (Size vs Price): {corr:.4f}")
print(f"Regression Line: Price = {model.coef_[0]:.3f} * Size + {model.intercept_:.2f}")
print(f"R² Score: {r2_score(price, pred):.4f}")
print(f"Root Mean Squared Error (RMSE): ${np.sqrt(mean_squared_error(price, pred)):.2f}k")
