import numpy as np
from collections import deque

def find_blank_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == '':
                return i, j

def possible_moves(state):
    moves = []
    i, j = find_blank_tile(state)
    if i > 0:
        moves.append('up')
    if i < len(state) - 1:
        moves.append('down')
    if j > 0:
        moves.append('left')
    if j < len(state[0]) - 1:
        moves.append('right')
    return moves

def do_move(state, action):
    new_state = [row[:] for row in state]
    i, j = find_blank_tile(state)
    if action == "up":
        new_state[i-1][j], new_state[i][j] = new_state[i][j], new_state[i-1][j]
    if action == "down":
        new_state[i+1][j], new_state[i][j] = new_state[i][j], new_state[i+1][j]
    if action == "left":
        new_state[i][j-1], new_state[i][j] = new_state[i][j], new_state[i][j-1]
    if action == "right":
        new_state[i][j+1], new_state[i][j] = new_state[i][j], new_state[i][j+1]
    return new_state

def return_heuristic(current_state, final_state):
    count = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != final_state[i][j] and current_state[i][j] != '':
                count += 1
    return count

def is_goal(state, final_state):
    return np.array_equal(state, final_state)

def iterative_deepening_search(initial_state, final_state):
    depth_limit = 0
    while True:
        result, nodes_expanded, nodes_generated, max_queue_length = depth_limited_search(initial_state, final_state, depth_limit)
        if result is not None:
            return result, nodes_expanded, nodes_generated, max_queue_length
        depth_limit += 1



def depth_limited_search(initial_state, final_state, depth_limit):
    open_list = deque([(initial_state, 0)])
    closed_list = set()
    nodes_expanded = 0
    nodes_generated = 0
    max_queue_length = 0

    while open_list:
        current_state, depth = open_list.popleft()
        closed_list.add(tuple(map(tuple, current_state)))

        if is_goal(current_state, final_state):
            return current_state, nodes_expanded, nodes_generated, max_queue_length

        if depth < depth_limit:
            for move in possible_moves(current_state):
                new_state = do_move(current_state, move)
                nodes_generated += 1
                if tuple(map(tuple, new_state)) not in closed_list:
                    open_list.append((new_state, depth + 1))
                    max_queue_length = max(max_queue_length, len(open_list))
        nodes_expanded += 1

    return None, nodes_expanded, nodes_generated, max_queue_length


initial_state = [[8, 2, ''],
                 [3, 4, 7],
                 [5, 1, 6]]

final_state = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, '']] 


print("Iterative Deepening Search:")
solutions, nodes_expanded, nodes_generated, max_queue_length = iterative_deepening_search(initial_state, final_state)
print("Solution found:")
for row in solutions:
    print(row)

print("Nodes Expanded:", nodes_expanded)
print("Nodes Generated:", nodes_generated)
print("Max Queue Length:", max_queue_length)