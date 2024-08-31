import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error

class MachineLearningCore:
    """
    Machine Learning Core for predictive modeling and decision-making.

    Attributes:
    -----------
    data : pandas.DataFrame
        Data to train and test machine learning models.
    """

    def __init__(self, data):
        self.data = data

    def train_linear_regression_model(self, X, y):
        """
        Train a linear regression model on the given data.

        Parameters:
        -----------
        X : pandas.DataFrame
            Feature data.
        y : pandas.Series
            Target data.

        Returns:
        -------
        model : sklearn.linear_model.LinearRegression
            Trained linear regression model.
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model

    def train_random_forest_classifier(self, X, y):
        """
        Train a random forest classifier model on the given data.

        Parameters:
        -----------
        X : pandas.DataFrame
            Feature data.
        y : pandas.Series
            Target data.

        Returns:
        -------
        model : sklearn.ensemble.RandomForestClassifier
            Trained random forest classifier model.
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model

    def evaluate_model(self, model, X_test, y_test):
        """
        Evaluate the performance of a trained machine learning model.

        Parameters:
        -----------
        model : sklearn.base.BaseEstimator
            Trained machine learning model.
        X_test : pandas.DataFrame
            Test feature data.
        y_test : pandas.Series
            Test target data.

        Returns:
        -------
        metrics : dict
            Dictionary containing evaluation metrics (e.g., accuracy, MSE).
        """
        y_pred = model.predict(X_test)
        if hasattr(model, "predict_proba"):
            y_pred_proba = model.predict_proba(X_test)
            metrics = {"accuracy": accuracy_score(y_test, y_pred), "auc": roc_auc_score(y_test, y_pred_proba[:, 1])}
        else:
            metrics = {"mse": mean_squared_error(y_test, y_pred)}
        return metrics
