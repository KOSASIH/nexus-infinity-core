import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class ArtificialIntelligenceCore:
    """
    Artificial Intelligence Core for decision-making and problem-solving.

    Attributes:
    -----------
    ai_model : sklearn.ensemble.RandomForestClassifier
        Artificial intelligence model for decision-making.
    """

    def __init__(self):
        self.ai_model = RandomForestClassifier(n_estimators=100)

    def train_ai_model(self, data, labels):
        """
        Train the artificial intelligence model using the provided data and labels.

        Parameters:
        -----------
        data : numpy.array
            Training data.
        labels : numpy.array
            Training labels.

        Returns:
        -------
        trained_model : sklearn.ensemble.RandomForestClassifier
            Trained artificial intelligence model.
        """
        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
        self.ai_model.fit(X_train, y_train)
        return self.ai_model

    def make_decision(self, input_data):
        """
        Make a decision using the trained artificial intelligence model.

        Parameters:
        -----------
        input_data : numpy.array
            Input data for decision-making.

        Returns:
        -------
        decision : int
            Decision made by the artificial intelligence model.
        """
        decision = self.ai_model.predict(input_data)
        return decision

    def solve_problem(self, problem_data):
        """
        Solve a problem using the trained artificial intelligence model.

        Parameters:
        -----------
        problem_data : numpy.array
            Problem data to solve.

        Returns:
        -------
        solution : int
            Solution to the problem made by the artificial intelligence model.
        """
        solution = self.ai_model.predict(problem_data)
        return solution
