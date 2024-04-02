from State import State
from queue import PriorityQueue

def AStar_search(given_state , n):
    GENERATED = 1 
    EXPANDED = 0
    max_queue_size = 1
    frontier = PriorityQueue() 
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    evaluation = root.Misplaced_Tiles(n) #we can use Manhattan_Distance() instead.
    frontier.put((evaluation[1], counter, root)) #based on A* evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        EXPANDED += 1
        print(f"explored: {EXPANDED:,}")
        if current_node.test():
            return current_node.solution(), EXPANDED, GENERATED, max_queue_size

        children = current_node.expand(n)
        GENERATED += 1
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Misplaced_Tiles(n) #we can use Manhattan_Distance() instead.
                frontier.put((evaluation[1], counter, child)) #based on A* evaluation
                if frontier.qsize() > max_queue_size:
                    max_queue_size = frontier.qsize()
    return None, EXPANDED, GENERATED, max_queue_size
