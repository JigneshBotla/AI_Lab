from depth_limit_UNINFORMED import depth_limited_search 
import numpy as np

NODES_EXPANDED = 0
NODES_GENERATED = 1

def iterative_deepn(initial_state,final_state):
    global NODES_EXPANDED, NODES_GENERATED
    depth = 1
    solution = None
    while True:
        solution, nodes_expanded, nodes_generated, max_queue_length = depth_limited_search(initial_state, final_state, depth)
        NODES_EXPANDED += nodes_expanded
        NODES_GENERATED += nodes_generated
        if solution is not None:
            return solution, NODES_EXPANDED, NODES_GENERATED, max_queue_length
        depth += 1

initial_state = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8]]

final_state = [[1, 2, 5],
               [3, 4, 8],
               [6, 7, 0]]

solution, nodes_expanded, nodes_generated, max_queue_length = iterative_deepn(initial_state, final_state)

if solution is not None:
    solutions = (np.array(state) for state in solution)
    print("Solution found within depth limit:")
    for row in solutions:
        print(row)
        print()

    print(f"Nodes expanded: {NODES_EXPANDED}")
    print(f"Nodes generated: {NODES_GENERATED}")
    print(f"Maximum queue length: {max_queue_length}")
else:
    print("Solution not found within depth limit.")
