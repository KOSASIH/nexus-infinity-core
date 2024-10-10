import os
import sys
from crossover_operators import *
from mutation_operators import *

def main():
    print("Nexus Infinity Evolution Utils")

    # Load configuration
    config = {}
    with open(os.path.join(os.path.dirname(__file__), "config.json"), "r") as f:
        config = json.load(f)

    # Initialize crossover operators
    crossover_operators = {
        "single_point": SinglePointCrossover(config["crossover_probability"]),
        "two_point": TwoPointCrossover(config["crossover_probability"]),
        "uniform": UniformCrossover(config["crossover_probability"]),
    }

    # Initialize mutation operators
    mutation_operators = {
        "gaussian": GaussianMutation(config["mutation_probability"], config["mutation_sigma"]),
        "uniform": UniformMutation(config["mutation_probability"], config["mutation_low"], config["mutation_high"]),
        "binary": BinaryMutation(config["mutation_probability"]),
        "swap": SwapMutation(config["mutation_probability"]),
        "insert": InsertMutation(config["mutation_probability"]),
        "delete": DeleteMutation(config["mutation_probability"]),
        "scramble": ScrambleMutation(config["mutation_probability"]),
    }

    # Run evolution process
    def evolve(population, generations):
        for _ in range(generations):
            offspring = []
            for _ in range(len(population)):
                parent1, parent2 = random.sample(population, 2)
                child1, child2 = crossover_operators["uniform"].crossover(parent1, parent2)
                child1 = mutation_operators["gaussian"].mutate(child1)
                child2 = mutation_operators["gaussian"].mutate(child2)
                offspring.extend([child1, child2])
            population = offspring
        return population

    # Example usage
    population = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    evolved_population = evolve(population, 10)
    print("Evolved Population:", evolved_population)

if __name__ == "__main__":
    main()
