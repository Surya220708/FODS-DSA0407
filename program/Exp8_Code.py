
import pandas as pd

sales_data = pd.DataFrame({
    'product_name': ['Pen', 'Book', 'Pencil',
                     'Pen', 'Book', 'Bag', 'Scale'],
    'quantity_sold': [50, 30, 40, 20, 25, 15, 10]
})

top_products = (
    sales_data.groupby('product_name')['quantity_sold']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("Top 5 Best-Selling Products:")
print(top_products)
