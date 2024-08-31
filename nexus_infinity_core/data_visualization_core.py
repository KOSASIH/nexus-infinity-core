import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DataVisualizationCore:
    """
    Data Visualization Core for insights and pattern discovery.

    Attributes:
    -----------
    data : pandas.DataFrame
        Data to visualize.
    """

    def __init__(self, data):
        self.data = data

    def visualize_distribution(self, column):
        """
        Visualize the distribution of a specific column.

        Parameters:
        -----------
        column : str
            Column to visualize.

        Returns:
        -------
        plot : matplotlib.pyplot.figure
            Distribution plot.
        """
        plt.figure(figsize=(10, 6))
        sns.distplot(self.data[column])
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        return plt

    def visualize_correlation(self):
        """
        Visualize the correlation between columns.

        Returns:
        -------
        plot : matplotlib.pyplot.figure
            Correlation plot.
        """
        corr_matrix = self.data.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
        plt.title("Correlation Matrix")
        return plt

    def visualize_scatterplot(self, x, y):
        """
        Visualize the relationship between two columns.

        Parameters:
        -----------
        x : str
            X-axis column.
        y : str
            Y-axis column.

        Returns:
        -------
        plot : matplotlib.pyplot.figure
            Scatterplot.
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=x, y=y, data=self.data)
        plt.title(f"Relationship between {x} and {y}")
        plt.xlabel(x)
        plt.ylabel(y)
        return plt
