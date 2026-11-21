import numpy as np

sales_data = np.array([125000, 138000, 152000, 171000])

total_sales = np.sum(sales_data)
pct_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("=== A2: Quarterly Sales ===")
print(f"Total Sales for the Year: ₹{total_sales}")
print(f"Percentage Increase (Q1 to Q4): {pct_increase:.2f}%")

