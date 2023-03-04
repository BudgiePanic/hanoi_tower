class Agent:
    # constructor
    def __init__(self, board, goal_state):
        self.goalState = goal_state
        self.frontier = [board]
    
    def solveDFS(self):
        # create a visited set
        visited = set()
        while self.frontier.count is not 0:
            board = self.frontier.pop()
            if board.state == self.goalState:
                return self.backtrack(board)
            visited.add(board)
            for move in board.generatePossibleMoves():
                if move.apply(board) not in visited:
                    self.frontier.append(move.apply(board))
        return []    

    def solveBFS(self):
        # create a visited set
        visited = set()
        while self.frontier.count is not 0:
            board = self.frontier.pop(0)
            if board.state == self.goalState:
                return self.backtrack(board)
            visited.add(board)
            for move in board.generatePossibleMoves():
                if move.apply(board) not in visited:
                    self.frontier.append(move.apply(board))
        return []
    
    def backtrack(self, board):
        moves = [board]
        while board.parent is not None:
            moves.append(board.parent)
            board = board.parent
        return moves