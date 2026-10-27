
import pandas as pd

order_data = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102],
    'order_date': ['2026-01-10', '2026-01-12',
                   '2026-01-15', '2026-01-18',
                   '2026-01-20'],
    'product_name': ['Pen', 'Book', 'Pen',
                     'Pencil', 'Book'],
    'order_quantity': [5, 2, 3, 4, 6]
})

order_data['order_date'] = pd.to_datetime(
    order_data['order_date']
)

print("Orders per Customer:")
print(order_data.groupby('customer_id').size())

print("\nAverage Quantity per Product:")
print(order_data.groupby('product_name')
      ['order_quantity'].mean())

print("\nEarliest Order:",
      order_data['order_date'].min())

print("Latest Order:",
      order_data['order_date'].max())
