from queue import PriorityQueue
import numpy as np


class State:
    goal = [[1, 2, 5],
            [3, 4, 8],
            [6, 7, 0]]

    def __init__(self, state, parent, direction, depth, cost):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth
        self.cost = cost
        if parent:
            self.cost = parent.cost + cost
        else:
            self.cost = cost

    def test(self):  
        return self.state == self.goal

    def Misplaced_Tiles(self, n):
        self.heuristic = sum(1 if self.state[i][j] != self.goal[i][j] else 0 for i in range(n) for j in range(n))
        self.AStar_evaluation = self.heuristic + self.cost
        return self.heuristic, self.AStar_evaluation
    

    # def Manhattan_Distance(self, n):
    #     self.heuristic = 0
    #     for i in range(n):
    #         for j in range(n):
    #             if self.state[i][j] != 0:
    #                 x, y = divmod(self.state[i][j] - 1, n)
    #                 self.heuristic += abs(x - i) + abs(y - j)

    #     self.greedy_evaluation = self.heuristic
    #     self.AStar_evaluation = self.heuristic + self.cost

    #     return self.greedy_evaluation, self.AStar_evaluation


    @staticmethod
    def eliminate_neighbours(x, n):
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n - 1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n * n - 1:
            moves.remove('Down')
        return moves

    def expand(self, n):
        x, y = next((i, j) for i in range(n) for j in range(n) if self.state[i][j] == 0)
        moves = self.eliminate_neighbours(x * n + y, n)
        children = []
        for direction in moves:
            temp = [row[:] for row in self.state]
            if direction == 'Left':
                temp[x][y], temp[x][y - 1] = temp[x][y - 1], temp[x][y]
            elif direction == 'Right':
                temp[x][y], temp[x][y + 1] = temp[x][y + 1], temp[x][y]
            elif direction == 'Up':
                temp[x][y], temp[x - 1][y] = temp[x - 1][y], temp[x][y]
            elif direction == 'Down':
                temp[x][y], temp[x + 1][y] = temp[x + 1][y], temp[x][y]
            children.append(State(temp, self, direction, self.depth + 1, 1))
        return children

    def solution(self):
        solution = [self.direction]
        path = self
        while path.parent is not None:
            path = path.parent
            solution.append(path.direction)
        solution = solution[:-1]
        solution.reverse()
        return solution

def AStar_search(initial_state, n):
    GENERATED = 1 
    EXPANDED = 0
    max_queue_size = 1
    frontier = PriorityQueue() 
    explored = set()
    counter = 0
    root = State(initial_state, None, None, 0, 0)
    evaluation = root.Manhattan_Distance(n)
    frontier.put((evaluation[1], counter, root)) 

    while not frontier.empty():
        current_node = frontier.get()[2]  
        EXPANDED += 1
        explored.add(tuple(map(tuple, current_node.state)))  
        if current_node.test():
            return explored, EXPANDED, GENERATED, max_queue_size

        children = current_node.expand(n)
        GENERATED += len(children)
        for child in children:
            if tuple(map(tuple, child.state)) not in explored:
                counter += 1
                evaluation = child.Misplaced_Tiles(n)
                frontier.put((evaluation[1], counter, child))  
                max_queue_size = max(max_queue_size, frontier.qsize())

    return None, EXPANDED, GENERATED, max_queue_size


initial_state = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8]]

final_state = [[1, 2, 5],
               [3, 4, 8],
               [6, 7, 0]]

print("\nA* using Misplaced Tile Heuristic:")
solution, nodes_expanded, nodes_generated, max_queue_length = AStar_search(initial_state, 3)
if solution:
    solutions = (np.array(state) for state in solution)
    print("Solution found:")
    for row in solutions:
        print(row)
        print()
else:
    print("No solution found.")
print("Nodes Expanded:", nodes_expanded)
print("Nodes Generated:", nodes_generated)
print("Max Queue Length:", max_queue_length)
