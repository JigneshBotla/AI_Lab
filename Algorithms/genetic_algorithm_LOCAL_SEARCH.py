import random

def fitness_fun(binarynum):
    return binarynum.count("1")

def single_point_crossover(binarynum1, binarynum2):
    crossover_point = len(binarynum1) // 2
    return binarynum1[:crossover_point] + binarynum2[crossover_point:], binarynum2[:crossover_point] + binarynum1[crossover_point:]

def bit_flip_mutation(binarynum):
    binary_list = list(binarynum)
    for i in range(len(binary_list)):
        if binary_list[i] == "0":
            binary_list[i] = "1"
            break
    return ''.join(binary_list)

def do_genetic(initial_population):
    fitness_values = [fitness_fun(individual) for individual in initial_population]
    while True:
        print("Initial Population:", initial_population)
        selected_indices = random.sample(range(len(initial_population)), 2)
        print("Selected candidates are :")
        print("Child 1:", initial_population[selected_indices[0]])
        print("Child 2:", initial_population[selected_indices[1]])
        parent1, parent2 = initial_population[selected_indices[0]], initial_population[selected_indices[1]]
        child1, child2 = single_point_crossover(parent1, parent2)
        child1 = bit_flip_mutation(child1)
        child2 = bit_flip_mutation(child2)
        print("After Crossover and Mutation:")
        print("Child 1:", child1)
        print("Child 2:", child2)
        if fitness_fun(child1) == len(child1):
            return True
        if fitness_fun(child2) == len(child2):
            return True
        initial_population[selected_indices[0]] = child1
        initial_population[selected_indices[1]] = child2

initial_population = ["0011", "1000", "1001", "1100"]
result = do_genetic(initial_population)
if result:
    print("Found a solution!")
else:
    print("No solution found within the given constraints.")
