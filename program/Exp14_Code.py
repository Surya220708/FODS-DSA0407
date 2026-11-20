import pandas as pd

data = {
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Age': [25, 30, 25, 42, 30, 22, 25, 42]
}

df = pd.DataFrame(data)
age_freq = df['Age'].value_counts().sort_index()

print("Customer Age Frequency Distribution:")
print(age_freq)
print(f"\nTotal Customers: {len(df)}")
print(f"Most common age: {df['Age'].mode()[0]} years")
