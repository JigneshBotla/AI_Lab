from State import State
from queue import LifoQueue

def DFS(given_state , n, limit):
    root = State(given_state, None, None, 0, 0)
    EXPANDED = 0
    GENERATED = 1
    max_queue_size = 1
    if root.test():
        return root.solution(),0,1,1
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    max_depth = 0
    while not(frontier.empty()):
        current_node = frontier.get()
        max_depth = current_node.depth #current depth

        print(f"current depth: {max_depth}")
        explored.append(current_node.state)


        if max_depth == limit:
            continue #go to the next branch

        children = current_node.expand(n)
        EXPANDED+=1

        for child in children:
            GENERATED+=1
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
                if frontier.qsize() > max_queue_size:
                    max_queue_size = frontier.qsize()
    return (("Couldn't find solution in the limited depth."), len(explored))
