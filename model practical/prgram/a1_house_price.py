import numpy as np

# Load house_data.csv (Columns: Bedrooms, Square Footage, Sale Price)
house_data = np.loadtxt("house_data.csv", delimiter=",", skiprows=1)

# Filter houses with more than 4 bedrooms and compute average sale price
more_than_4 = house_data[house_data[:, 0] > 4]
avg_price = np.mean(more_than_4[:, 2])

print("=== A1: House Price Analysis ===")
print(f"Average Sale Price (>4 bedrooms): ₹{avg_price:.2f} lakh")

