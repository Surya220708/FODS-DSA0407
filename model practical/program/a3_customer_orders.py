import pandas as pd

order_data = pd.DataFrame({
    "Customer ID": ["C101", "C102", "C101", "C103", "C102", "C104", "C101", "C103", "C104", "C105"],
    "Order Date": pd.to_datetime([
        "2024-01-05", "2024-01-07", "2024-01-12", "2024-01-15", "2024-01-20",
        "2024-01-22", "2024-02-02", "2024-02-08", "2024-02-14", "2024-02-20"
    ]),
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Mouse", "Laptop", "Headphones", "Mouse", "Keyboard", "Laptop", "Headphones"],
    "Order Quantity": [1, 3, 2, 5, 1, 2, 4, 1, 2, 3]
})

print("=== A3: Customer Orders ===")
print("1. Total orders per customer:")
print(order_data.groupby("Customer ID").size())

print("\n2. Average order quantity per product:")
print(order_data.groupby("Product Name")["Order Quantity"].mean().round(2))

print(f"\n3. Earliest Order Date: {order_data['Order Date'].min().date()}")
print(f"   Latest Order Date:   {order_data['Order Date'].max().date()}")

