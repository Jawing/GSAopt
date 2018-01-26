#!/usr/bin/python
"""define gameTable object"""

import numpy as np
#import math
#import pickle

#gameboard
class Board:
    #constructor 
    goal = np.array([[0, 1, 2], [5, 4, 3]])
    #TODO auto goal location
    #ys = game.board.shape[0]
    #xs = game.board.shape[1]
    #goalLocation = [np.where(game.goal == x) for x in range(ys*xs))]  
    goalLocation = [(0,0),(1,0),(2,0),(2,1),(1,1),(0,1)]
    def __init__(self, board):
        self.board = board
        self.emptyCell = np.where(self.board == 0)
