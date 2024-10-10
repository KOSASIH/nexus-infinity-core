def selection_method_1(population, fitness_values):
    # Select parents using a simple roulette wheel selection
    total_fitness = sum(fitness_values)
    selection_probabilities = [fitness / total_fitness for fitness in fitness_values]
    parents = []
    for _ in range(len(population) // 2):
        parent = random.choices(population, weights=selection_probabilities)[0]
        parents.append(parent)
    return parents

def selection_method_2(population, fitness_values):
    # Select parents using a more complex tournament selection
    tournament_size = 3
    parents = []
    for _ in range(len(population) // 2):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=lambda individual: fitness_values[population.index(individual)])
        parents.append(winner)
    return parents

# Register selection methods
SelectionMethods = {
    'selection_method_1': selection_method_1,
    'selection_method_2': selection_method_2
}
