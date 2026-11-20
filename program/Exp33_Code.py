import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

data = {
    'engine_size': [1.6, 2.0, 2.5, 3.0, 3.5, 2.0, 1.8, 4.0],
    'horsepower': [120, 160, 200, 260, 300, 175, 140, 380],
    'mpg': [34, 28, 24, 20, 18, 26, 30, 15],
    'price': [18000, 24000, 31000, 42000, 51000, 26000, 21000, 68000]
}
df = pd.DataFrame(data)
X = df[['engine_size', 'horsepower', 'mpg']]
y = df['price']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = LinearRegression().fit(X_scaled, y)

importance = pd.Series(model.coef_, index=X.columns).sort_values(ascending=False)
print("Automobile Price Linear Regression Modeling:")
print(f"Model R² Score: {model.score(X_scaled, y):.4f}")
print("\nInfluential Factors Affecting Car Prices (Standardized Coeffs):")
for feat, coef in importance.items():
    print(f"{feat:<15}: {coef:+.2f}")
