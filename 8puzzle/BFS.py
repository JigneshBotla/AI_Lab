from queue import Queue
from State import State


def BFS(given_state, n):
    root = State(given_state, None, None, 0, 0)
    EXPANDED = 0
    GENERATED = 0
    max_size = 0
    if root.test():
        print(f"No. of nodes generated: <{GENERATED:,}>")
        print(f"No. of nodes expanded: <{EXPANDED:,}>")
        print(f"Max size of frontier: <{max_size}>")
        return root.solution()
    frontier = Queue()

    frontier.put(root)
    explored = []
    while not (frontier.empty()):
        size = frontier.qsize()
        if size > max_size:
            max_size = size
        current_node = frontier.get()
        explored.append(current_node.state)
        children = current_node.expand(n)
        EXPANDED += 1
        for child in children:
            GENERATED += 1
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                print(f"explored: {EXPANDED:,}")
                print(f"generated: {GENERATED:,}")

                frontier.put(child)
    return
