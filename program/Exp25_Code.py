from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

acc = accuracy_score(y_test, clf.predict(X_test))
sample_input = [[5.1, 3.5, 1.4, 0.2]]
pred_species = iris.target_names[clf.predict(sample_input)[0]]

print("Decision Tree Iris Classification:")
print(f"Model Accuracy on Test Set: {acc*100:.2f}%")
print(f"Sample Flower Dimensions: {sample_input[0]}")
print(f"Predicted Species: {pred_species}")
