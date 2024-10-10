def fitness_function_1(individual):
    # Calculate fitness using a simple function
    return individual[0] ** 2 + individual[1] ** 2

def fitness_function_2(individual):
    # Calculate fitness using a more complex function
    return individual[0] ** 2 + 2 * individual[1] ** 2 + individual[0] * individual[1]

# Register fitness functions
FitnessFunctions = {
    'fitness_function_1': fitness_function_1,
    'fitness_function_2': fitness_function_2
}
