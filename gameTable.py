#!/usr/bin/python
"""define gameTable object"""

import numpy as np
#import math
#import pickle

#gameboard
class Board:
    #constructor 
    goal = np.array([[0, 1, 2], [5, 4, 3]])
    """ scalable goal location
    ys = game.board.shape[0]
    xs = game.board.shape[1]
    goalLocation = [np.where(game.goal == x) for x in range(ys*xs))]  
    """
    goalLocation = [(0,0),(1,0),(2,0),(2,1),(1,1),(0,1)]
    def __init__(self, board):
        self.board = board
        self.emptyCell = np.where(self.board == 0)

#cost heuristic +x+y distance away from location
def manhattanCost(game):
    cost = 0
    for y in range(game.board.shape[0]):
        for x in range(game.board.shape[1]):
            current = game.board[y,x]
            #NOTE for admissability do not take account the 0 position
            if current != 0:
                xf, yf = game.goalLocation[current]
                cost += abs(xf - x) + abs(yf - y)
    return cost

#cost heuristic +1 for wrong tile location
def naiveCost(game):
    cost = 0
    for y in range(game.board.shape[0]):
        for x in range(game.board.shape[1]):
            current = game.board[y,x]
            #NOTE for admissability do not take account the 0 position
            if game.goalLocation[current] != (x, y) and current != 0:
                cost += 1
    return cost
#multiplied by the weight of the move
def manhattanCostWeighted(game):
    cost = 0
    for y in range(game.board.shape[0]):
        for x in range(game.board.shape[1]):
            current = game.board[y,x]
            #NOTE for admissability do not take account the 0 position
            if current != 0:
                xf, yf = game.goalLocation[current]
                cost += current * (abs(xf - x) + abs(yf - y))
    return cost
def NoCost(game):
    return 0