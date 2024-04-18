import random
import math

connect_cities = {}
dist_cities = {}

def TSP_obj(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += dist_cities.get((route[i], route[i+1]), 0)
    total_distance += dist_cities.get((route[-1], route[0]), 0)  
    return total_distance

def generate_initial_states(k, n):
    initial_states = []
    for _ in range(k):
        initial_route = list(range(1, n + 1))
        random.shuffle(initial_route)
        initial_states.append(initial_route)
    return initial_states

def generate_successors(states):
    successors = []
    for state in states:
        for _ in range(len(state)):
            city1, city2 = random.sample(range(1, len(state)), 2)
            next_route = state[:]
            next_route[city1], next_route[city2] = next_route[city2], next_route[city1]
            successors.append(next_route)
    return successors

def select_best_k(successors, k):
    sorted_successors = sorted(successors, key=TSP_obj)
    return sorted_successors[:k]

def Local_Beam_Search(k, n, max_iterations=2000, initial_temperature=1000, cooling_rate=0.003):
    current_states = generate_initial_states(k, n)
    temperature = initial_temperature
    while temperature > 0.1:
        successors = generate_successors(current_states)
        best_k = select_best_k(successors, k)
        if any(TSP_obj(route) == 0 for route in best_k):
            return [route for route in best_k if TSP_obj(route) == 0][0]  
        else:
            for state in current_states:
                next_state = random.choice(best_k)
                delta_E = TSP_obj(next_state) - TSP_obj(state)
                if delta_E < 0 or random.uniform(0, 1) < math.exp(-delta_E / temperature):
                    state[:] = next_state[:]
        temperature *= 1 - cooling_rate
    return None 

n = int(input("Enter the total cities which salesman wants to travel: "))

for i in range(1, n + 1):
    temp = []
    x = int(input("Enter the number of cities connected to city-" + str(i) + ": "))
    if x > n - 1:
        print("Error in the route mapping of cities.")
        break
    if x > 0:
        print("Enter the cities:")
        for j in range(x):
            y = int(input())
            if y == i:
                print("Salesman can't travel to the same city!")
                break
            temp.append(y)
    connect_cities[i] = temp

print("Connected cities are :" + str(connect_cities))

print("Enter the distances between cities:")
for i in range(1, n + 1):
    for j in range(len(connect_cities[i])):
        print(str(i) + "------>" + str(connect_cities[i][j]) + ":")
        z = float(input())
        dist_cities[(i, connect_cities[i][j])] = z

print("Distance between connected cities are :" + str(dist_cities))

k = int(input("Enter the number of states: "))
optimized_route = Local_Beam_Search(k, n)
if optimized_route:
    print("Optimized route:", optimized_route)
    print("Total distance:", TSP_obj(optimized_route))
else:
    print("No solution found within the maximum iterations.")
