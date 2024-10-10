import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Normal, Categorical
from .utils import FitnessFunctions, SelectionMethods, MutationOperators, CrossoverOperators

class EvolutionStrategy:
    def __init__(self, config):
        self.config = config
        self.fitness_function = FitnessFunctions[config['fitness_function']]
        self.selection_method = SelectionMethods[config['selection_method']]
        self.mutation_operator = MutationOperators[config['mutation_operator']]
        self.crossover_operator = CrossoverOperators[config['crossover_operator']]
        self.population_size = config['population_size']
        self.generations = config['generations']
        self.elite_size = config['elite_size']
        self.sigma = config['sigma']
        self.learning_rate = config['learning_rate']
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.population = self.initialize_population()
        self.elite = self.initialize_elite()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = self.initialize_individual()
            population.append(individual)
        return population

    def initialize_individual(self):
        individual = {
            'params': self.initialize_params(),
            'fitness': 0.0
        }
        return individual

    def initialize_params(self):
        params = []
        for _ in range(self.config['num_params']):
            param = Normal(0, self.sigma).sample()
            params.append(param)
        return params

    def initialize_elite(self):
        elite = []
        for _ in range(self.elite_size):
            individual = self.initialize_individual()
            elite.append(individual)
        return elite

    def evolve(self):
        for generation in range(self.generations):
            self.evaluate_population()
            self.select_elite()
            self.mutate_elite()
            self.crossover_elite()
            self.update_population()

    def evaluate_population(self):
        for individual in self.population:
            fitness = self.fitness_function(individual['params'])
            individual['fitness'] = fitness

    def select_elite(self):
        self.elite = self.selection_method(self.population, self.elite_size)

    def mutate_elite(self):
        for individual in self.elite:
            individual['params'] = self.mutation_operator(individual['params'], self.sigma)

    def crossover_elite(self):
        offspring = []
        for _ in range(self.elite_size):
            parent1, parent2 = random.sample(self.elite, 2)
            child1, child2 = self.crossover_operator(parent1['params'], parent2['params'])
            offspring.extend([child1, child2])
        self.elite = offspring

    def update_population(self):
        self.population = self.elite + self.population[self.elite_size:]

    def get_best_individual(self):
        best_individual = max(self.population, key=lambda individual: individual['fitness'])
        return best_individual

    def get_best_fitness(self):
        best_fitness = max(individual['fitness'] for individual in self.population)
        return best_fitness
