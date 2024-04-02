from Astar import AStar_search
from time import time

n = int(input("Enter n\n"))
print("Enter your", n, "*", n, "puzzle")
root = []
for i in range(0, n * n):
    p = int(input())
    root.append(p)

for j in range(0, n * n):
    print(f'{root[j]} ', end='')
    if (j+1) % n == 0:
        print(' ')
time1 = time()
AStar_solution = [] 
AStar_solution, explored, expanded, generated = AStar_search(root, n)
time = time() - time1
if AStar_solution is not None:
    print('Solution is ', AStar_solution)
    print('Number of explored nodes is ', explored)
    print('Size of the solution is ', len(AStar_solution))
    print('Time:', time, "\n")
 