import pandas as pd
import numpy as np

df = pd.read_csv("stock_data.csv")
prices = df['Close']

mean_price = prices.mean()
variance = prices.var()
std_dev = prices.std()
price_range = prices.max() - prices.min()
cv = (std_dev / mean_price) * 100

print("Stock Price Variability Analysis:")
print(f"Observations Count : {len(prices)} trading days")
print(f"Mean Closing Price : ${mean_price:.2f}")
print(f"Price Variance     : {variance:.4f}")
print(f"Standard Deviation : ${std_dev:.2f}")
print(f"Price Range        : ${price_range:.2f} (Min: ${prices.min():.2f}, Max: ${prices.max():.2f})")
print(f"Coefficient of Var : {cv:.2f}%")
