import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class DecisionTree:
    def __init__(self, max_depth, min_samples_split, min_samples_leaf):
        self.tree = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)

    def fit(self, X, y):
        self.tree.fit(X, y)

    def predict(self, X):
        return self.tree.predict(X)

class RandomForest:
    def __init__(self, n_estimators, max_depth, min_samples_split, min_samples_leaf):
        self.forest = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)

    def fit(self, X, y):
        self.forest.fit(X, y)

    def predict(self, X):
        return self.forest.predict(X)

class GradientBoostingMachine:
    def __init__(self, n_estimators, learning_rate, max_depth, min_samples_split, min_samples_leaf):
        self.gbm = GradientBoostingClassifier(n_estimators=n_estimators, learning_rate=learning_rate, max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)

    def fit(self, X, y):
        self.gbm.fit(X, y)

    def predict(self, X):
        return self.gbm.predict(X)

# Example usage:
X = np.random.rand(100, 10)  # Replace with your feature data
y = np.random.randint(0, 2, 100)  # Replace with your target data

dt = DecisionTree(max_depth=5, min_samples_split=2, min_samples_leaf=1)
dt.fit(X, y)
y_pred = dt.predict(X)
print("Decision Tree Accuracy:", accuracy_score(y, y_pred))

rf = RandomForest(n_estimators=10, max_depth=5, min_samples_split=2, min_samples_leaf=1)
rf.fit(X, y)
y_pred = rf.predict(X)
print("Random Forest Accuracy:", accuracy_score(y, y_pred))

gbm = GradientBoostingMachine(n_estimators=10, learning_rate=0.1, max_depth=5, min_samples_split=2, min_samples_leaf=1)
gbm.fit(X, y)
y_pred = gbm.predict(X)
print("Gradient Boosting Machine Accuracy:", accuracy_score(y, y_pred))
