import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Features: [Systolic BP, Blood Glucose, Heart Rate]
X = np.array([
    [120, 85, 72], [140, 140, 85], [118, 90, 70], [150, 160, 92],
    [125, 95, 75], [160, 180, 88], [115, 80, 68], [145, 150, 82],
    [130, 110, 78], [155, 170, 95]
])
# Labels: 0 = No Condition, 1 = Condition Detected
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

new_patient = np.array([[135, 130, 80]])
pred = knn.predict(new_patient)[0]
prob = knn.predict_proba(new_patient)[0]

print(f"KNN Classifier (k={k}):")
print(f"New Patient Symptoms: BP=135, Glucose=130, HR=80")
print(f"Predicted Diagnosis: {'Condition Detected (1)' if pred == 1 else 'Healthy (0)'}")
print(f"Prediction Probability: No Condition: {prob[0]*100:.1f}%, Condition: {prob[1]*100:.1f}%")
