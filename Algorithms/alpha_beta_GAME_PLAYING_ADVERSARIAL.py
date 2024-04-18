import math
import random

class Node:
    def __init__(self, value=None, depth=0):
        self.value = value
        self.depth = depth
        self.children = []

def construct_tree(depth, maximizingPlayer):
    if depth == 0 or (depth == 1 and not maximizingPlayer):  
        return Node(heuristic_value(maximizingPlayer))  

    node = Node(depth=depth)
    for i in range(2):  
        node.children.append(construct_tree(depth - 1, not maximizingPlayer))

    return node

def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or not node.children:  
        return node.value

    if maximizingPlayer:
        value = float('-inf')
        for child in node.children:
            value = max(value, alphabeta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break 
        return value
    else:  
        value = float('inf')
        for child in node.children:
            value = min(value, alphabeta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  
        return value

def heuristic_value(maximizingPlayer):
    if maximizingPlayer == True:
        return 1
    else:
        return -1

def pick_sticks(n, i, stick_count):
    if n >= 1 and n <= 3:
        if stick_count - n > 1:
            stick_count -= n
        elif stick_count - n == 1:
            print("Player " + str(i) + " won the game!!")
            return 1, stick_count
        else:
            print("Please do a valid pickup!!")
    else:
        print("Please do a valid pickup!!")
    return 0, stick_count

def AI_bot_pick_sticks(stick_count):
    depth = min(3, stick_count - 1) 
    maximizingPlayer = True 
    origin = construct_tree(depth, maximizingPlayer)

    optimal_value = float('-inf')
    optimal_move = 1
    alpha = float('-inf')
    beta = float('inf')
    for i, child in enumerate(origin.children):
        value = alphabeta(child, depth - 1, alpha, beta, False)
        if value > optimal_value:
            optimal_value = value
            optimal_move = i + 1
        alpha = max(alpha, value)

    return optimal_move

stick_count = 5
win = 0

while win != 1:
    print("---- PLAYER ----")
    n1 = int(input("Enter the no of sticks you want to pick: "))
    win, stick_count = pick_sticks(n1, "Player", stick_count)
    if win == 1:
        break

    print("---- AI_BOT ----")
    n2 = AI_bot_pick_sticks(stick_count)
    print("AI_Bot picked", n2, "sticks")
    win, stick_count = pick_sticks(n2, "AI_BOT", stick_count)
    if win == 1:
        break
