class State:
    goal = [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

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


    def test(self):  # check if the given state is goal
        if self.state == self.goal:
            return True
        return False
    
    def Misplaced_Tiles(self ,n):
            self.heuristic = 0
            for i in range(1 , n*n):
                distance = abs(self.state.index(i) - self.goal.index(i))

                #manhattan distance between the current state and goal state
                self.heuristic = self.heuristic + distance/n + distance%n

            self.greedy_evaluation = self.heuristic
            self.AStar_evaluation = self.heuristic + self.cost

            return( self.greedy_evaluation, self.AStar_evaluation)

    def Manhattan_Distance(self,n):
            counter = 0;
            self.heuristic = 0
            for i in range(n*n):
                for j in range(n*n):
                    if (self.state[i] != self.goal[j]):
                        counter += 1
                    self.heuristic = self.heuristic + counter

            self.greedy_evaluation = self.heuristic
            self.AStar_evaluation = self.heuristic + self.cost

            return( self.greedy_evaluation, self.AStar_evaluation)

    @staticmethod
    # remove illegal moves for a given state
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

    # produces children of a given state
    def expand(self, n):
        x = self.state.index(0)
        moves = self.eliminate_neighbours(x, n)

        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]

            children.append(
                State(temp, self, direction, self.depth + 1, 1))  # depth should be changed as children are produced
        return children

    # gets the given state and returns its direction + it's parent's direction till there is no parent
    def solution(self):
        solution = [self.direction]
        path = self
        while path.parent is not None:
            path = path.parent
            solution.append(path.direction)
        solution = solution[:-1]
        solution.reverse()
        return solution
