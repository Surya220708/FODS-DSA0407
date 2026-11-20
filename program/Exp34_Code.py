import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Features: [Age, Gender (1=M, 0=F), Systolic BP, Cholesterol]
X = np.array([
    [45, 1, 130, 210], [52, 0, 140, 240], [38, 1, 120, 180], [65, 0, 160, 270],
    [41, 0, 125, 195], [58, 1, 150, 250], [35, 1, 118, 175], [62, 0, 155, 260],
    [49, 1, 135, 220], [55, 0, 145, 230]
])
# Outcome: 1 = "Good", 0 = "Bad"
y = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print("Medical Research Treatment Outcome (KNN Classifier):")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred)*100:.1f}%")
print("\nPredictions on Test Patients:")
for actual, pred in zip(y_test, y_pred):
    act_str = "Good" if actual == 1 else "Bad"
    prd_str = "Good" if pred == 1 else "Bad"
    print(f"Actual: {act_str:<5} | Predicted: {prd_str}")
