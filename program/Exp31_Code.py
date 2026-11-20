import numpy as np
from sklearn.cluster import KMeans

# Features: [Monthly Spend ($), Browsing Hours, Returns Count]
X = np.array([
    [120, 5, 0], [140, 6, 1], [800, 25, 2], [950, 30, 1],
    [300, 12, 1], [350, 14, 2], [1100, 35, 3], [150, 7, 0],
    [400, 15, 1], [750, 22, 2]
])

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)

print("E-commerce Customer Segmentation Analysis:")
for i, center in enumerate(kmeans.cluster_centers_):
    print(f"Cluster {i}: Spend=${center[0]:.1f}, Browsing={center[1]:.1f} hrs, Returns={center[2]:.1f}")
print("\nTargeting Strategies:")
print("Cluster 0: Regular Low-Spenders -> Offer discount promotions")
print("Cluster 1: Moderate Shoppers   -> Recommend loyalty programs")
print("Cluster 2: Premium High-Spenders -> Provide VIP exclusive offers")
