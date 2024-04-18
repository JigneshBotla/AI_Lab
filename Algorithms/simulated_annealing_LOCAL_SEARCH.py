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

def Simulated_Annealing(current_route, initial_temperature=1000, cooling_rate=0.003):
    current = current_route[:]
    temperature = initial_temperature
    while temperature > 0.1:
        next_route = current[:]
        city1, city2 = random.sample(range(1, len(current)), 2)
        next_route[city1], next_route[city2] = next_route[city2], next_route[city1]
        
        delta_E = TSP_obj(next_route) - TSP_obj(current)
        if delta_E < 0:
            current = next_route[:]
        else:
            if random.uniform(0, 1) < math.exp(-delta_E / temperature):
                current = next_route[:]
        temperature *= 1 - cooling_rate
    return current

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

print("Connected cities are :"+str(connect_cities))

print("Enter the distances between cities:")
for i in range(1, n + 1):
    for j in range(len(connect_cities[i])):
        print(str(i) + "------>" + str(connect_cities[i][j]) + ":")
        z = float(input())
        dist_cities[(i, connect_cities[i][j])] = z

print("Distance between connected cities are :"+str(dist_cities))

initial_route = list(range(1, n + 1))
random.shuffle(initial_route)

print("Initial route:", initial_route)
optimized_route = Simulated_Annealing(initial_route)
print("Optimized route:", optimized_route)
print("Total distance:", TSP_obj(optimized_route))
