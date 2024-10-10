from .evolutionary_algorithms import GeneticAlgorithm, EvolutionStrategy
from .machine_learning import NeuralNetworks, DeepLearning, ReinforcementLearning

class Evolution:
    def __init__(self, config):
        self.config = config
        self.algorithm = self.select_algorithm()

    def select_algorithm(self):
        if self.config['algorithm'] == 'genetic':
            return GeneticAlgorithm(self.config)
        elif self.config['algorithm'] == 'evolution_strategy':
            return EvolutionStrategy(self.config)
        elif self.config['algorithm'] == 'machine_learning':
            return NeuralNetworks(self.config)
        else:
            raise ValueError('Invalid algorithm selection')

    def evolve(self, population):
        return self.algorithm.evolve(population)
