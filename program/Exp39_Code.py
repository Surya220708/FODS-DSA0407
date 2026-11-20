import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Features: [Total Amount Spent ($), Number of Items Purchased]
X = np.array([
    [150, 3], [180, 4], [210, 5], [500, 15], [550, 18],
    [620, 16], [1200, 35], [1350, 40], [1400, 38], [1100, 32]
])

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

print("E-commerce K-Means Customer Clustering:")
for i, c in enumerate(centers):
    print(f"Cluster {i} Centroid: Spend=${c[0]:.1f}, Items={c[1]:.1f}")

plt.figure(figsize=(7, 4))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=60, edgecolors='k')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("Customer Segmentation Clusters")
plt.xlabel("Total Amount Spent ($)")
plt.ylabel("Number of Items Purchased")
plt.legend()
plt.savefig("exp39_plot.png")
print("Cluster visualization plot saved to exp39_plot.png.")
