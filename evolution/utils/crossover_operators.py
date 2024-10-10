import numpy as np

class CrossoverOperator:
    def __init__(self, crossover_probability):
        self.crossover_probability = crossover_probability

    def crossover(self, parent1, parent2):
        if np.random.rand() < self.crossover_probability:
            crossover_point = np.random.randint(1, len(parent1) - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            return child1, child2
        else:
            return parent1, parent2

class SinglePointCrossover(CrossoverOperator):
    def __init__(self, crossover_probability):
        super().__init__(crossover_probability)

class TwoPointCrossover(CrossoverOperator):
    def __init__(self, crossover_probability):
        super().__init__(crossover_probability)

    def crossover(self, parent1, parent2):
        if np.random.rand() < self.crossover_probability:
            crossover_point1 = np.random.randint(1, len(parent1) - 1)
            crossover_point2 = np.random.randint(crossover_point1, len(parent1) - 1)
            child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
            child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]
            return child1, child2
        else:
            return parent1, parent2

class UniformCrossover(CrossoverOperator):
    def __init__(self, crossover_probability):
        super().__init__(crossover_probability)

    def crossover(self, parent1, parent2):
        if np.random.rand() < self.crossover_probability:
            child1 = [parent1[i] if np.random.rand() < 0.5 else parent2[i] for i in range(len(parent1))]
            child2 = [parent2[i] if np.random.rand() < 0.5 else parent1[i] for i in range(len(parent2))]
            return child1, child2
        else:
            return parent1, parent2
