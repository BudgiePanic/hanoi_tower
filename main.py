from agent import Agent
from board import Board


initial_state = [[5,4,3,2,1], [], []]
goal_state = [[], [], [5,4,3,2,1]]

# make a board object
board = Board(initial_state)

agent = Agent(board, goal_state)

moves = agent.solveDFS()

# movesBFS = agent.solveBFS()

for move in moves:
    print(move,"\n")

# Sanity check
# print(board.isValid())
# print(board.generatePossibleMoves())