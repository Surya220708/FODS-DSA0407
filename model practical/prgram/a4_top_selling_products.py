import pandas as pd

sales_df = pd.DataFrame({
    "OrderID": list(range(1, 17)),
    "Product": [
        "Pen", "Notebook", "Bag", "Pen", "Marker", "Notebook", "Stapler", "Bag",
        "Folder", "Pen", "Calculator", "Marker", "Diary", "Notebook", "Folder", "Calculator"
    ],
    "Quantity": [25, 40, 8, 30, 15, 22, 10, 12, 18, 20, 6, 9, 14, 18, 11, 9]
})

top5 = sales_df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)

print("=== A4: Top Selling Products ===")
print("Top 5 Best-Selling Products:")
print(top5)

