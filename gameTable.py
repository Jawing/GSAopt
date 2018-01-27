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
            xf, yf = game.goalLocation[game.board[y,x]]
            cost += abs(xf - x) + abs(yf - y)
    return cost

#cost heuristic +1 for wrong tile location
def naiveCost(game):
    cost = 0
    for y in range(game.board.shape[0]):
        for x in range(game.board.shape[1]):
            if game.goalLocation[game.board[y,x]] != (x, y):
                cost += 1
    return cost

def NoCost(game):
    return 0