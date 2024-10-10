import numpy as np

class MutationOperator:
    def __init__(self, mutation_probability):
        self.mutation_probability = mutation_probability

    def mutate(self, individual):
        if np.random.rand() < self.mutation_probability:
            return self._mutate(individual)
        else:
            return individual

    def _mutate(self, individual):
        raise NotImplementedError("Subclasses must implement the _mutate method")

class GaussianMutation(MutationOperator):
    def __init__(self, mutation_probability, sigma):
        super().__init__(mutation_probability)
        self.sigma = sigma

    def _mutate(self, individual):
        return [x + np.random.normal(0, self.sigma) for x in individual]

class UniformMutation(MutationOperator):
    def __init__(self, mutation_probability, low, high):
        super().__init__(mutation_probability)
        self.low = low
        self.high = high

    def _mutate(self, individual):
        return [np.random.uniform(self.low, self.high) if np.random.rand() < self.mutation_probability else x for x in individual]

class BinaryMutation(MutationOperator):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def _mutate(self, individual):
        return [1 - x if np.random.rand() < self.mutation_probability else x for x in individual]

class SwapMutation(MutationOperator):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def _mutate(self, individual):
        i, j = np.random.choice(len(individual), 2, replace=False)
        individual[i], individual[j] = individual[j], individual[i]
        return individual

class InsertMutation(MutationOperator):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def _mutate(self, individual):
        i = np.random.randint(len(individual))
        individual.insert(i, np.random.rand())
        return individual

class DeleteMutation(MutationOperator):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def _mutate(self, individual):
        if len(individual) > 1:
            i = np.random.randint(len(individual))
            del individual[i]
        return individual

class ScrambleMutation(MutationOperator):
    def __init__(self, mutation_probability):
        super().__init__(mutation_probability)

    def _mutate(self, individual):
        i, j = np.random.choice(len(individual), 2, replace=False)
        individual[i:j] = individual[i:j][::-1]
        return individual
