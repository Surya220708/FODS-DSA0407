import numpy as np
from sklearn.cluster import KMeans

# Features: [Annual Income ($k), Spending Score (1-100)]
X = np.array([
    [15, 39], [16, 81], [17, 6], [18, 77], [20, 40],
    [55, 49], [60, 55], [65, 52], [70, 58], [75, 54],
    [90, 85], [95, 90], [100, 88], [110, 92], [115, 86]
])

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

new_customer = np.array([[62, 50]])
cluster_id = kmeans.predict(new_customer)[0]

print("K-Means Customer Segmentation:")
print(f"New Customer Input: Income=$62k, Spending Score=50")
print(f"Assigned Cluster: Group {cluster_id}")
print(f"Cluster Centers (Income, Spending):\n{kmeans.cluster_centers_.round(1)}")
