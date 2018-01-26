#!/usr/bin/python
"""define gameTable object"""

import numpy as np
#import math
#import pickle

#gameboard
class Board:
    #constructor 
    def __init__(self, board):
        self.board = board
        self.emptyCell = np.where(self.board == 0)
