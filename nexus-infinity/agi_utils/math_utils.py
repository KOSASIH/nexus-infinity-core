import numpy as np
import scipy.stats as stats
from scipy.optimize import minimize

def calculate_mean(numbers):
    return np.mean(numbers)

def calculate_median(numbers):
    return np.median(numbers)

def calculate_mode(numbers):
    return stats.mode(numbers)[0][0]

def calculate_standard_deviation(numbers):
    return np.std(numbers)

def calculate_variance(numbers):
    return np.var(numbers)

def calculate_correlation_coefficient(x, y):
    return np.corrcoef(x, y)[0, 1]

def calculate_regression_line(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, c

def optimize_function(func, initial_guess, bounds):
    res = minimize(func, initial_guess, method="SLSQP", bounds=bounds)
    return res.x

def generate_random_numbers(size, distribution="normal", **kwargs):
    if distribution == "normal":
        return np.random.normal(kwargs["mean"], kwargs["stddev"], size)
    elif distribution == "uniform":
        return np.random.uniform(kwargs["low"], kwargs["high"], size)
    else:
        raise ValueError("Invalid distribution")

# Example usage:
numbers = [1, 2, 3, 4, 5]
mean = calculate_mean(numbers)
print("Mean:", mean)

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
m, c = calculate_regression_line(x, y)
print("Regression Line: y = {:.2f}x + {:.2f}".format(m, c))
