from DFS import DFS

def iterative_deepening(board):
    for depth in range(8):
        DFS(board, 0, depth)
