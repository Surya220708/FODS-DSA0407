import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

data = {
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'amount_spent': [450, 120, 2200, 3100, 180, 2800, 500, 160, 3400, 600],
    'frequency': [12, 3, 25, 30, 4, 28, 14, 5, 32, 15]
}
df = pd.DataFrame(data)
X = df[['amount_spent', 'frequency']]

kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
df['Segment'] = kmeans.fit_predict(X)

print("Retail Customer Segmentation (K-Means):")
for seg in range(2):
    subset = df[df['Segment'] == seg]
    print(f"Segment {seg} (Count={len(subset)}): Avg Spend=${subset['amount_spent'].mean():.1f}, Avg Visits={subset['frequency'].mean():.1f}")
