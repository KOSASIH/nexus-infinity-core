import random
from .utils import FitnessFunctions, SelectionMethods, MutationOperators, CrossoverOperators

class GeneticAlgorithm:
    def __init__(self, config):
        self.config = config
        self.fitness_function = FitnessFunctions[config['fitness_function']]
        self.selection_method = SelectionMethods[config['selection_method']]
        self.mutation_operator = MutationOperators[config['mutation_operator']]
        self.crossover_operator = CrossoverOperators[config['crossover_operator']]

    def evolve(self, population):
        # Evaluate fitness
        fitness_values = [self.fitness_function(individual) for individual in population]

        # Select parents
        parents = self.selection_method(population, fitness_values)

        # Crossover
        offspring = []
        for _ in range(self.config['crossover_rate']):
            parent1, parent2 = random.sample(parents, 2)
            child1, child2 = self.crossover_operator(parent1, parent2)
            offspring.extend([child1, child2])

        # Mutate
        for individual in offspring:
            if random.random() < self.config['mutation_rate']:
                individual = self.mutation_operator(individual)

        return offspring
